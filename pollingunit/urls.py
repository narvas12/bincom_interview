from django.urls import path
from . import views

urlpatterns = [
    path('pollingunit/', views.polling_unit_results, name='individual_polling_unit'),
]
