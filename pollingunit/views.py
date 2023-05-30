from django.shortcuts import render
from .models import AnnouncedPuResults
from .models import PollingunitAnnouncedlgaresult


def announced_pu_results(request):
    results = AnnouncedPuResults.objects.all()
    return render(request, 'individual_pu_result.html', {'results': results})



def summed_total_result(request):
    lgas = PollingunitAnnouncedlgaresult.objects.values_list('lga_name', flat=True).distinct()
    selected_lga = request.GET.get('lga', None)

    if selected_lga:
        total_result = PollingunitAnnouncedlgaresult.objects.filter(lga_name=selected_lga).aggregate(Sum('party_score'))
    else:
        total_result = None

    context = {
        'lgas': lgas,
        'selected_lga': selected_lga,
        'total_result': total_result,
    }

    return render(request, 'myapp/summed_total_result.html', context)
