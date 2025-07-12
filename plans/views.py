from django.shortcuts import render
from .models import Subscribe

# Used code from Boutique Ado


def all_plans(request):
    """ A view to show all products, including sorting queries """

    plans = Subscribe.objects.all()
    nutrition_plans = Subscribe.objects.filter(category='nutrition')
    exercises_plans = Subscribe.objects.filter(category='exercises')

    context = {
        'plans': plans,
        'nutrition_plans': nutrition_plans,
        'exercises_plans': exercises_plans,
    }

    return render(request, 'plans/plans.html', context)