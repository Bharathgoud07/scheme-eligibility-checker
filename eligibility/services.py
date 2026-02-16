from documents.models import UserDocument


def check_eligibility(user_profile, scheme):

    # Safety guard (prevents crash)
    if not user_profile:
        return {
            "status": "not_eligible",
            "missing_documents": [],
            "reasons": ["Profile not found"]
        }

    missing_documents = []
    ineligibility_reasons = []
    status = "eligible"

    criteria = scheme.eligibility_criteria or {}

    # AGE
    if "min_age" in criteria and user_profile.age < criteria["min_age"]:
        ineligibility_reasons.append(f"Minimum age is {criteria['min_age']}")
        status = "not_eligible"

    if "max_age" in criteria and user_profile.age > criteria["max_age"]:
        ineligibility_reasons.append(f"Maximum age is {criteria['max_age']}")
        status = "not_eligible"

    # INCOME
    if "max_income" in criteria and user_profile.annual_income > criteria["max_income"]:
        ineligibility_reasons.append("Income exceeds allowed limit")
        status = "not_eligible"

    # FLAGS
    if criteria.get("requires_bpl") and not user_profile.bpl:
        ineligibility_reasons.append("Only BPL families allowed")
        status = "not_eligible"

    if criteria.get('requires_farmer') and not getattr(user_profile, "is_farmer", False):
        ineligibility_reasons.append("Only farmers allowed")
        status = "not_eligible"

    # Check if woman based on gender
    is_woman = user_profile.gender.lower() in ['f', 'female', 'w', 'woman']
    if criteria.get("requires_woman") and not is_woman:
        ineligibility_reasons.append("Only women allowed")
        status = "not_eligible"

    # Check if student based on education level
    is_student = user_profile.education_level in ['10th', '12th', 'UG', 'PG']
    if criteria.get("requires_student") and not is_student:
        ineligibility_reasons.append("Only students allowed")
        status = "not_eligible"

    # DOCUMENT CHECK (REAL CHECK)
    required_docs = scheme.documents.filter(is_required=True)

    user_docs = UserDocument.objects.filter(profile=user_profile).values_list("document_id", flat=True)

    for doc in required_docs:
        if doc.id not in user_docs:
            missing_documents.append({
                "name": doc.name,
                "description": doc.description
            })

    if missing_documents and status == "eligible":
        status = "documents_missing"

    return {
        "status": status,
        "missing_documents": missing_documents,
        "reasons": ineligibility_reasons
    }
