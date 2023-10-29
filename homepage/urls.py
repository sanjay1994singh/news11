from django.urls import path
from .import views
urlpatterns = [
    path('homepage/', views.home_page, name='home_page'),
    path('', views.main_homepage, name='main_homepage'),
    path('details/<int:id>/', views.details, name='details'),
    path('follow/', views.follow, name='follow'),
    path('watching-views/', views.watching_views, name='watching_views'),
    path('watch-views/', views.watch_views, name='watch_views'),
]
