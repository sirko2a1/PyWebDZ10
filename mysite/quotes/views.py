from django.shortcuts import render
from django.http import HttpResponse

def start_page(request):
    return render(request, 'quotes/start_page.html')