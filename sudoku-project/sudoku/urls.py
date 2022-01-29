from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('gameplay/', views.gameplay),
    path("signup/", views.SignUp.as_view(), name="signup"),
]