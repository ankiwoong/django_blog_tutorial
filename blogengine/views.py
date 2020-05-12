from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from blogengine.models import Post


def getPosts(request, selected_page=1):
    # Get all blog posts
    posts = Post.objects.all().order_by('-pub_date')
    # Add pagination
    pages = Paginator(posts, 5)
    returned_page = pages.page(selected_page)
    # Display all the posts
    return render(request, 'posts.html', {'posts': returned_page.object_list})
