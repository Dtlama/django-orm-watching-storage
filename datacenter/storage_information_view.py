from datacenter.models import Passcard
from datacenter.models import Visit, format_duration, get_visit_duration
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for visit in visits:
        non_closed_visit = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_visit_duration(visit)),
            }
        non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
