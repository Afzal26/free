from django.urls import path, include
from freelance import views
urlpatterns = [

    path('index/', views.index, name='index'),

]