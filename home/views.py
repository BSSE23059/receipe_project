from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    peoples = [
        {'Name': 'Muhammad Hazim', 'Age': 19},
        {'Name': 'Ibrahim AbdulSattar', 'Age': 17},
        {'Name': 'Arslan Sultan', 'Age': 20},
        {'Name': 'Saim Saleem', 'Age': 19},
        {'Name': 'Murtaza Saleem', 'Age': 19},
    ]

    vegetables = ['Pumpkins', 'Tomatoes', 'Potatoes']

    for people in peoples:
        print(people)

    return render(request, "home/index.html", context={'page':'Django Tutorial 2024','peoples': peoples, 'vegetables': vegetables})

def about(request):
    context = {'page' : 'About'}
    return render(request, "home/about.html" , context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request, "home/contact.html" , context)


def success_page(request):
    return HttpResponse("<h1>Hi! This is a success page.</h1>")
