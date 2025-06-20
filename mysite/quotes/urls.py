from django.urls import path
from . import views

#conf
urlpatterns = [
    path('start/', views.start_page)
]