from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def home(request):
    return HttpResponse("Hello world!")


def about(request):
    return HttpResponse("about")


def contact(request):
    return HttpResponse("contact")


def ex_html(request):
    template = loader.get_template('exampleTemplate.html')
    return HttpResponse(template.render())


