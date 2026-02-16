from django.shortcuts import render
from profiles.models import UserProfile
from .models import Scheme
from .services import check_eligibility


def results(request):
    # Get the profile for the current logged-in user if available, otherwise get the first profile
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user_profile = UserProfile.objects.first()
    else:
        user_profile = UserProfile.objects.first()
    
    schemes = Scheme.objects.all()

    schemes_with_status = []
    eligible_count = 0
    documents_missing_count = 0
    not_eligible_count = 0

    for scheme in schemes:
        eligibility = check_eligibility(user_profile, scheme)

        schemes_with_status.append({
            "name": scheme.name,
            "ministry": scheme.ministry,
            "description": scheme.description,
            "benefits": scheme.benefits,
            "eligible_status": eligibility["status"],
            "missing_documents": eligibility["missing_documents"],
            "ineligibility_reasons": eligibility["reasons"],
            "category": scheme.category,
            "scheme_category": scheme.scheme_category,
            "target_group": scheme.target_group,
        })

        # Count status
        if eligibility["status"] == "eligible":
            eligible_count += 1
        elif eligibility["status"] == "documents_missing":
            documents_missing_count += 1
        else:
            not_eligible_count += 1

    # Get unique categories and scheme categories for filters
    categories = sorted(
        list(
            set([
                scheme["category"] for scheme in schemes_with_status
                if scheme["category"]
            ])
        )
    )

    scheme_categories = sorted(
        list(
            set([
                scheme["scheme_category"] for scheme in schemes_with_status
                if scheme["scheme_category"]
            ])
        )
    )

    # Define target group order as per target image
    target_group_order = [
        'Students', 'Women', 'Farmers', 'Minority', 'SC/ST', 'BPL',
        'Senior Citizens', 'Youth', 'General'
    ]

    return render(request, "eligibility/results.html", {
        "schemes": schemes_with_status,
        "categories": categories,
        "scheme_categories": scheme_categories,
        "target_group_order": target_group_order,
        "user_profile": user_profile,
        "eligible_count": eligible_count,
        "documents_missing_count": documents_missing_count,
        "not_eligible_count": not_eligible_count,
        "total_schemes": len(schemes_with_status),
    })
