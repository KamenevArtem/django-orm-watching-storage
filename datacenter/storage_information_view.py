import datetime
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def get_duration(visit):
    entered_time = localtime(visit.entered_at)
    leaved_time = localtime(visit.leaved_at)
    duration_of_visit = leaved_time - entered_time
    duration_time = int(duration_of_visit.total_seconds())
    return duration_time


def format_duration(duration_time):
    hours = duration_time // 3600
    minutes = (duration_time % 3600) // 60
    seconds = duration_time - (minutes * 60) - (hours * 3600)
    time_in_storage = f"{hours}:{minutes}:{seconds}"
    time_in_storage = datetime.datetime.strptime(time_in_storage, "%H:%M:%S")
    return datetime.datetime.strftime(time_in_storage, "%H:%M:%S")


def is_visit_long(duration):
    suspicious_time = 3600
    if duration > suspicious_time:
        return "Посещение подозрительное"
    else:
        return "Подозрений нет"


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in non_closed_visits:
        visit_time = get_duration(visit)
        duration_of_visit = format_duration(visit_time)
        is_strange = is_visit_long(visit_time)
        non_closed_visit = [
            {
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at,
                'duration': duration_of_visit,
                'is_strange': is_strange,
            }
        ]
        context = {
            'non_closed_visits': non_closed_visit, 
        }
    return render(request, 'storage_information.html', context)
