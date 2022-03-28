from django.urls import path
from . import views

urlpatterns = [
    #for returning webpages
    path('', views.index, name = 'index'),
    path('gameplay/', views.gameplay),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('stats/',views.stats, name='player stats'),

    #for server requests
    path('returnstats/', views.returnStats),
    path('addgamedata/', views.addGameData)
]

