from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import wine_details
# Create your views here.


def wines(request):
    context = {
        'wines': wine_details.objects.all()[:10]
    }
    return render(request, 'wine_details/index.html', context)


def wines_country(request):
    context = {
        'wines_country': wine_details.objects.order_by('country').reverse()[:10]
    }
    return render(request, 'wine_details/country.html', context)


def wines_province(request):
    context = {
        'wines_province': wine_details.objects.order_by('province').reverse()[:10]
    }
    return render(request, 'wine_details/province.html', context)


def wines_region_1(request):
    context = {
        'wines_region_1': wine_details.objects.order_by('region_1').reverse()[:10]
    }
    return render(request, 'wine_details/region_1.html', context)


def wines_region_2(request):
    context = {
        'wines_region_2': wine_details.objects.order_by('region_2').reverse()[:10]
    }
    return render(request, 'wine_details/region_2.html', context)


def wines_sort(request):
    context = {
        'wines_sort': wine_details.objects.order_by('price').reverse()[:10]
    }
    return render(request, 'wine_details/sort.html', context)


def wines_variety(request):
    context = {
        'wines_variety': wine_details.objects.order_by('variety').reverse()[:10]
    }
    return render(request, 'wine_details/variety.html', context)
