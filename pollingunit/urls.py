from django.urls import path
from .views import individual_polling_unit, lga_total_result, new_polling_unit_results

urlpatterns = [
    path('polling_unit/<int:unique_id>/', individual_polling_unit, name='individual_polling_unit'),
    path('lga_total_result/', lga_total_result, name='lga_total_result'),
    path('new_polling_unit_results/', new_polling_unit_results, name='new_polling_unit_results'),
]


