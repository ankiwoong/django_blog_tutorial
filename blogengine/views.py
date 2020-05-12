from django.shortcuts import render
from django.http import HttpResponse

from blogengine.models import Post


def getRecentPosts(request):
    # Get all blog posts
    posts = Post.objects.all()
    # Sort posts into chronological order
    sorted_posts = posts.order_by('-pub_date')
    # Display all the posts
    return render(request, 'posts.html', {'posts': sorted_posts})
