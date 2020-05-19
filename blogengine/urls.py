from django.urls import path, re_path

from . import views


appname = 'blogengine'

urlpatterns = [
    path('', views.getPosts),
    path('/blog/<int:selected_page>/', views.getPosts),
    re_path(r'^\d{4}/\d{1,2}/(?P<postSlug>[-a-zA-Z0-9]+)/?$', views.getPost),
]
