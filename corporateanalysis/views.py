from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def company_info(request):
    return render(request, template_name='company-info/index.html')


def search(request):
    return render(request, template_name='corporateanalysis/search/search.html')


def company_information(request):
    return render(request, template_name='corporateanalysis/search/company_information.html')


def index(request):
    return render(request, template_name='corporateanalysis/search/index.html')


def search_graph(request):
    return render(request, template_name='corporateanalysis/search/search_graph.html')


def search_table(request):
    return render(request, template_name='corporateanalysis/search/search_table.html')


def search_value(request):
    return render(request, template_name='corporateanalysis/search/search_value.html')


def comparison_menu(request):
    return render(request, template_name='corporateanalysis/comparison/comparison_menu.html')


def comparison_start(request):
    return render(request, template_name='corporateanalysis/comparison/comparison_start.html')


def comparison_result(request):
    return render(request, template_name='corporateanalysis/comparison/comparison_result.html')


def book_main(request):
    return render(request, template_name='corporateanalysis/book/book_main.html')


def star_main(request):
    return render(request, template_name='corporateanalysis/favorite/star_main.html')
