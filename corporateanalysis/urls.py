from django.urls import path
from .views import company_info, hello_world

app_name = 'corporateanalysis'

urlpatterns = [
    path('', hello_world, name='hello'),
    path('info/', company_info, name='info'),
]
