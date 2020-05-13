from django.urls import path

from . import views

urlpatterns = [
    path('', views.getPosts),
    path('<int:selected_page>/', views.getPosts),
]
