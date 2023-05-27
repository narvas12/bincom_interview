from django.shortcuts import render, redirect
from .models import PollingUnit, AnnouncedPuResults, Lga



# Create a view to fetch and display the result
def individual_polling_unit(request, unique_id):
    polling_unit = PollingUnit.objects.get(uniqueid=unique_id)
    results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=unique_id)
    context = {
        'polling_unit': polling_unit,
        'results': results,
    }
    return render(request, 'individual_pu.html', context)



# Create a to fetch and display the summed results:
def lga_total_result(request):
    lgas = Lga.objects.all()
    selected_lga_id = request.GET.get('lga_id')
    if selected_lga_id:
        polling_units = PollingUnit.objects.filter(lga_id=selected_lga_id)
        results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid__in=polling_units.values('uniqueid'))
        total_results = {}
        for result in results:
            if result.party_abbreviation not in total_results:
                total_results[result.party_abbreviation] = 0
            total_results[result.party_abbreviation] += result.party_score
    else:
        polling_units = None
        total_results = None
    context = {
        'lgas': lgas,
        'polling_units': polling_units,
        'total_results': total_results,
    }
    return render(request, 'lga_total_result.html', context)



# Create a to handle storing the results:
def new_polling_unit_results(request):
    if request.method == 'POST':
        unique_id = request.POST.get('unique_id')
        party_results = {}
        for party in ['PDP', 'DPP', 'ACN', 'PPA', 'CDC', 'JP']:
            party_score = request.POST.get(party)
            if party_score:
                party_results[party] = int(party_score)
        for party, score in party_results.items():
            result = AnnouncedPuResults.objects.create(
                polling_unit_uniqueid=unique_id,
                party_abbreviation=party,
                party_score=score
            )
        return redirect('individual_polling_unit', unique_id=unique_id)
    else:
        polling_units = PollingUnit.objects.all()
        context = {
            'polling_units': polling_units,
        }
        return render(request, 'new_pu_unit_results.html', context)


def new_polling_unit_results(request):
    if request.method == 'POST':
        unique_id = request.POST.get('unique_id')
        party_results = {}
        for party in ['PDP', 'DPP', 'ACN', 'PPA', 'CDC', 'JP']:
            party_score = request.POST.get(party)
            if party_score:
                party_results[party] = int(party_score)
        for party, score in party_results.items():
            result = AnnouncedPuResults.objects.create(
                polling_unit_uniqueid=unique_id,
                party_abbreviation=party,
                party_score=score
            )
        return redirect('individual_polling_unit', unique_id=unique_id)
    else:
        polling_units = PollingUnit.objects.all()
        context = {
            'polling_units': polling_units,
        }
        return render(request, 'new_pu_results.html', context)


