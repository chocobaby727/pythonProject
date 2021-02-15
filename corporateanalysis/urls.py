from django.urls import path
from .views import hello_world, search, comparison

app_name = 'corporateanalysis'

urlpatterns = [
    path('', hello_world, name='hello'),
    path('search/search.html', search, name='search'),
    path('comparison/comparison_menu.html', comparison, name='comparison_menu'),
]
