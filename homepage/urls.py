from django.urls import path
from .import views
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('homepage/', views.main_homepage, name='main_homepage'),
    path('follow/', views.follow, name='follow'),
    path('watching-views/', views.watching_views, name='watching_views'),
]
