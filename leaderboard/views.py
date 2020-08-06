from django.shortcuts import render
from market.models import Cars, Users


def leaderboard_index(request):

    leaderboard = Cars.objects.all().order_by("-car_power")[:20]

    context = {}
    context["leaderboard"] = leaderboard
    context["total_cars"] = 20

    return render(request, 'leaderboard/leaderboard_index.html', context)
