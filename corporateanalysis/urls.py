from django.urls import path
from .views import hello_world, corporateanalysis

app_name = 'corporateanalysis'

urlpatterns = [
    path('', hello_world, name='hello'),
    path('search/search.html', corporateanalysis, name='search'),
]
