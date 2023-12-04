from django.shortcuts import render, get_object_or_404
from .models import Blog


def post_list(request):
    post = Blog.published.all()
    return render(request, 'blog/post/list.html', {'posts': post})


def post_detail(request, id):
    post = get_object_or_404(Blog,
                             id=id,
                             status=Blog.Status.PUBLISHED)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})


