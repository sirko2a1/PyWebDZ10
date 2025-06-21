from django.shortcuts import render
from django.http import HttpResponse

def start_page(request):
    return render(request, 'start_page.html')