from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Subscribe


# Used code from Boutique Ado


def all_plans(request):
    """ A view to show all plans, including sorting queries """

    plans = Subscribe.objects.all()
    nutrition_plans = Subscribe.objects.filter(category='nutrition')
    exercise_plans = Subscribe.objects.filter(category='exercise')
    sort = None
    direction = None
    selected_levels = []
    selected_durations = []

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            nutrition_plans = nutrition_plans.order_by(sortkey)
            exercise_plans = exercise_plans.order_by(sortkey)

    # Filtering by duration
        if "duration_weeks" in request.GET and request.GET["duration_weeks"]:
            duration = int(request.GET["duration_weeks"])
            nutrition_plans = nutrition_plans.filter(duration_weeks=duration)
            exercise_plans = exercise_plans.filter(duration_weeks=duration)
            selected_durations = [duration]
        else:
            selected_durations = []  

        # Filtering by level
        if "level" in request.GET and request.GET["level"]:
            level = int(request.GET["level"])
            nutrition_plans = nutrition_plans.filter(level=level)
            exercise_plans = exercise_plans.filter(level=level)
            selected_levels = [level]
        else:
            selected_levels = []         

    current_sorting = f'{sort or "None"}_{direction or "None"}'

    all_durations = Subscribe.objects.values_list(
        "duration_weeks", flat=True
    ).distinct()

    all_levels = Subscribe._meta.get_field("level").choices             

    context = {
        'plans': plans,
        'nutrition_plans': nutrition_plans,
        'exercise_plans': exercise_plans,
        "current_sorting": current_sorting,
        "selected_levels": selected_levels,
        "selected_durations": selected_durations,
        "all_durations": all_durations,
        "all_levels": all_levels,
    }

    return render(request, 'plans/plans.html', context)


def plan_detail(request, plan_id):
    """ A view to show individual plan details """

    plan = get_object_or_404(Subscribe, pk=plan_id)

    context = {
        'plan': plan,
    }

    return render(request, 'plans/plan_detail.html', context)

