from django.urls import path
from . import views

urlpatterns = [
    path('announced-pu-results/', views.announced_pu_results, name='announced_pu_results'),
    path('summed-total-result/', views.summed_total_result, name='summed_total_result'),
]
