from django.urls import path, re_path

from . import views


appname = 'blogengine'

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    path('admin/', include(admin.site.urls)),

    # Home page
    path('', views.getPosts),
    path('<int:selected_page>/', views.getPosts),

    # Blog posts
    re_path(r'^\d{4}/\d{1,2}/(?P[-a-zA-Z0-9]+)/?$', views.getPost),

    # Categories
    path('categories/<slug:categorySlug>/', views.getCategory),
    path('categories/<slug:categorySlug>/<int:selected_page>/', views.getCategory)

    # Flat pages
    path('', include('django.contrib.flatpages.urls')),
]
