from django.shortcuts import render, redirect
from .models import UserProfile


def profile_form(request):

    if request.method == 'POST':

        name = request.POST.get('full_name')
        age = request.POST.get('age')
        income = request.POST.get('income')
        category = request.POST.get('category')
        education = request.POST.get('education')
        state = request.POST.get('state')
        gender = request.POST.get('gender')

        rural = True if request.POST.get('rural') else False
        bpl = True if request.POST.get('bpl') else False

        errors = []

        # validation
        if not name:
            errors.append("Full Name is required")

        try:
            age = int(age)
            if age <= 0:
                errors.append("Age must be greater than zero")
        except (ValueError, TypeError):
            errors.append("Enter a valid age")

        try:
            income = int(income)
            if income < 0:
                errors.append("Income cannot be negative")
        except (ValueError, TypeError):
            errors.append("Enter a valid income")

        if not category:
            errors.append("Category is required")

        if not education:
            errors.append("Education level is required")

        if not state:
            errors.append("State is required")

        if errors:
            return render(request, 'profiles/profile_form.html', {
                'errors': errors,
                'data': request.POST
            })

        profile = UserProfile.objects.create(
            name=name,
            age=age,
            annual_income=income,
            category=category,
            education_level=education,
            state=state,
            gender=gender,
            rural=rural,
            bpl=bpl
        )

        request.session['profile_id'] = profile.id

        return redirect('/documents/')

    return render(request, 'profiles/profile_form.html')
