from django.shortcuts import render
from .models import Subscribe

# Used code from Boutique Ado


def all_plans(request):
    """ A view to show all products, including sorting queries """

    plans = Subscribe.objects.all()

    context = {
        'plans': plans,
    }

    return render(request, 'plans/plans.html', context)