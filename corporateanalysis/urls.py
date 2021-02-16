from .views import hello_world, search, comparison
from .views import company_info, hello_world, search
from django.urls import path

app_name = 'corporateanalysis'

urlpatterns = [
    path('', hello_world, name='hello'),
    path('info/', company_info, name='info'),
    path('search/search.html', search, name='search'),
    path('comparison/comparison_menu.html',
         comparison, name='comparison_menu'),
]
