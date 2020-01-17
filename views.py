from django.shortcuts import render,HttpResponse
def homepage(request):
    return HttpResponse('welcome all')
def aboutpage(request):
    return HttpResponse('this is about page')

# Create your views here.
