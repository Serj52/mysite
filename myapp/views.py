from django.shortcuts import render
from django.http import HttpResponse
from .models import Producer, Festival, Category, Films, Recom
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

def search(request):
    if bool(request.GET.get('search')):
        try:
            res = Films.objects.get(name=request.GET.get('search'))
            return render(request, 'search.html', context={'res': res})
        except ObjectDoesNotExist:
            return render(request, 'not_found.html')

def home(requests):
         res = Category.objects.all()
         return render(requests, 'home.html', context={'res': res})


def fest(request):
    if request.GET.get('category') == 'Фестивальное кино':
        return render(request, 'fest.html', context={'res': Festival.objects.all})

    elif request.GET.get('category') == "Боевик" or request.GET.get('category') == "Комедия":
        res = Films.objects.filter(category__name=request.GET.get('category'))
        return render(request, 'base_film.html', context={'res': res})

    else:
        res = Films.objects.filter(Q(id=3) | Q(id=5))
        return render(request, 'base_film.html', context={'res': res})


def film(request):
    if request.GET.get('category') == 'Венецианский кинофестиваль':
        res = Films.objects.filter(festival_name__name=request.GET.get('category'))
        return render(request, 'base_film.html', context={'res': res})

    elif request.GET.get('category') == 'Канский кинофестиваль':
        res = Films.objects.filter(festival_name__name=request.GET.get('category'))
        return render(request, 'base_film.html', context={'res': res})


def contacts(requests):
    return render(requests, 'contacts.html')