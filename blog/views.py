from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django import template

# Create your views here.
def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})



register = template.Library()
