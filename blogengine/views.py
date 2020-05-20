from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

from blogengine.models import Post, Category


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
    return render(request, 'posts.html', {'posts': returned_page.object_list, 'page': returned_page})


def getPost(request, postSlug):
    # Get specified post
    post = Post.objects.filter(slug=postSlug)
    # Display specified post
    return render(request, 'single.html', {'posts': post})


def getCategory(request, categorySlug, selected_page=1):
    # Get specified category
    posts = Post.objects.all().order_by('-pub_date')
    category_posts = []
    for post in posts:
        if post.categories.filter(slug=categorySlug):
            category_posts.append(post)
    # Add pagination
    pages = Paginator(category_posts, 5)
    # Get the category
    category = Category.objects.filter(slug=categorySlug)[0]
    # Get the specified page
    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)
    # Display all the posts
    return render(request, 'category.html', {'posts': returned_page.object_list, 'page': returned_page, 'category': category})
