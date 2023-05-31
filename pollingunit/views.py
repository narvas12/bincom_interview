from django.shortcuts import render, redirect
from .models import *

def announced_pu_results(request):
    results = AnnouncedPuResults.objects.all()
    return render(request, 'individual_pu_result.html', {'results': results})




def summed_total_result(request):
    # Retrieve all the local governments
    local_governments = AnnouncedLgaResults.objects.all()

    if request.method == 'POST':
        selected_lga = request.POST.get('local_government')

        # Retrieve the polling unit results for the selected local government
        results = AnnouncedLgaResults.objects.filter(lga_name=selected_lga)

        # Calculate the summed total result
        total_result = sum(result.party_score for result in results)

        context = {
            'local_governments': local_governments,
            'selected_lga': selected_lga,
            'total_result': total_result,
        }

        return render(request, 'lga_total_result.html', context)

    context = {
        'local_governments': local_governments,
    }

    return render(request, 'lga_total_result.html', context)





def add_polling_unit_results(request):
    parties = Party.objects.all()
    polling_units = PollingUnit.objects.all()

    if request.method == 'POST':
        polling_unit_id = request.POST.get('polling_unit')
        for party in parties:
            party_abbreviation = party.partyid
            party_score = request.POST.get(f'party_{party_abbreviation}')

            PollingunitAnnouncedpuresult.objects.create(
                polling_unit_uniqueid=polling_unit_id,
                party_abbreviation=party_abbreviation,
                party_score=party_score,
                entered_by_user=request.user.username,  # Change if you have user authentication
                # Add other fields as necessary
            )

        return redirect('polling_unit_results')  # Redirect to a page after saving the results

    context = {
        'parties': parties,
        'polling_units': polling_units,
    }

    return render(request, 'new_pu_results.html', context)
