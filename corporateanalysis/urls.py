from .views import *
from django.urls import path

app_name = 'corporateanalysis'

urlpatterns = [
    path('', company_info, name='info'),
    path('info/', company_info, name='info'),
    path('search/search.html/', search, name='search'),
    path('search/company_information.html/', company_information, name='company_information'),
    path('search/index.html/', index, name='index'),
    path('search/search_graph.html/', search_graph, name='search_graph'),
    path('search/search_table.html/', search_table, name='search_table'),
    path('search/search_value.html/', search_value, name='search_value'),
    path('comparison/comparison_menu.html/',
         comparison_menu, name='comparison_menu'),
    path('comparison/comparison_start.html/',
         comparison_start, name='comparison_start'),
    path('comparison/comparison_result.html/',
         comparison_result, name='comparison_result'),
    path('book/book_main.html/',
         book_main, name='book_main'),
    path('favorite/star_main.html/',
         star_main, name='star_main'),
]
