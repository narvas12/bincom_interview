from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import PollingUnit, PollingunitAnnouncedpuresult


def polling_unit_results(request, polling_unit_id):
    try:
        polling_unit = PollingUnit.objects.get(uniqueid=polling_unit_id)
        results = PollingunitAnnouncedpuresult.objects.filter(polling_unit_uniqueid=polling_unit_id)
        
        context = {
            'polling_unit': polling_unit,
            'results': results
        }
        
        return render(request, 'individual_pu_result.html', context)
    
    except PollingUnit.DoesNotExist:
        # Handle the case when polling unit doesn't exist
        return HttpResponse('polling unit not found')



