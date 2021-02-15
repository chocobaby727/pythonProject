from django.urls import path
<<<<<<< HEAD
from .views import company_info, hello_world
=======
from .views import hello_world, corporateanalysis
>>>>>>> master

app_name = 'corporateanalysis'

urlpatterns = [
    path('', hello_world, name='hello'),
<<<<<<< HEAD
    path('info/', company_info, name='info'),
=======
    path('search/search.html', corporateanalysis, name='search'),
>>>>>>> master
]
