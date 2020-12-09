from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def homepage_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})


def contacts_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {"my_text": "this is about me",
                  "my_number": 123,
                  "my_list": [1, 2, 3],
                  "this_is_true": True,
                  "title": "some title"}
    return render(request, "about.html", my_context)
