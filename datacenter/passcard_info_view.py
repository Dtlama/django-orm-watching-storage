from datacenter.models import Passcard, get_visit_duration, format_duration, is_visit_suspicious
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in visits:
        this_passcard_visit = {
            'entered_at': visit.entered_at,
            'duration': format_duration(get_visit_duration(visit)),
            'is_strange': is_visit_suspicious(get_visit_duration(visit)),
            }
    this_passcard_visits.append(this_passcard_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
