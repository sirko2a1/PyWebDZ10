from django.urls import path
from . import views

#conf
urlpatterns = [
    path('', views.start_page, name='start'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.confirm_logout_view, name='logout'),
]