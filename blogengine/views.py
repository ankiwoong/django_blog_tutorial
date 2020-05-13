from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

from blogengine.models import Post


def getPosts(request, selected_page=1):
    # Get all blog posts
    posts = Post.objects.all().order_by('-pub_date')
    # Add pagination
    pages = Paginator(posts, 5)
    # Get the specified page
    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)
    # Display all the posts
    return render(request, 'posts.html', {'posts': returned_page.object_list})


def getPost(request, postSlug):
    # Get specified post
    post = Post.objects.filter(slug=postSlug)
    # Display specified post
    return render(request, 'posts.html', {'posts': post})
