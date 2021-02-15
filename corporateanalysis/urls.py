from django.urls import path
from .views import company_info, hello_world, corporateanalysis

app_name = 'corporateanalysis'

urlpatterns = [
    path('', hello_world, name='hello'),
    path('info/', company_info, name='info'),
    path('search/search.html', corporateanalysis, name='search'),
]
