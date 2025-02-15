from django.urls import path
from . import views


urlpatterns = [
    #path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('<int:id>/', views.post, name='post'),
    path('search/', views.search, name='search'),
    path('tag/<int:id>/',views.tag, name='tag'),
    #path('google/', views.google)
] 