from django.shortcuts import render
from .models import Subscribe

# Used code from Boutique Ado


def all_plans(request):
    """ A view to show all products, including sorting queries """

    plans = Subscribe.objects.all()
    nutrition_plans = Subscribe.objects.filter(category='nutrition')
    exercise_plans = Subscribe.objects.filter(category='exercise')

    context = {
        'plans': plans,
        'nutrition_plans': nutrition_plans,
        'exercise_plans': exercise_plans,
    }

    return render(request, 'plans/plans.html', context)