from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datacenter.storage_information_view import get_duration
from datacenter.storage_information_view import format_duration
from datacenter.storage_information_view import is_visit_long


def passcard_info_view(request, passcode):
    get_object_or_404(Passcard, pk=1)
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    passcarde_visits = []
    for visit in visits:
        duration_of_visit = int(get_duration(visit))
        is_visit_suspicious = is_visit_long(duration_of_visit)  
        this_passcard_visits = {
                'entered_at': visit.entered_at,
                'duration': format_duration(duration_of_visit),
                'is_strange': is_visit_suspicious
            }
        passcarde_visits.append(this_passcard_visits)
    context = {
        'passcard': passcard,
       'this_passcard_visits': passcarde_visits
    }
    return render(request, 'passcard_info.html', context)
