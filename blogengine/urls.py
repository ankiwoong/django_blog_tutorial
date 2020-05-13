from django.urls import path, re_path

from . import views


appname = 'blogengine'

urlpatterns = [
    path('', views.getPosts),
    path('<int:selected_page>/', views.getPosts),
    path('<str:postSlug>/', views.getPost),
]
