from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
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


def plan_detail(request, plan_id):
    """ A view to show individual plan details """

    plan = get_object_or_404(Subscribe, pk=plan_id)

    context = {
        'plan': plan,
    }

    return render(request, 'plans/plan_detail.html', context)