from django.http import HttpResponse
from django.shortcuts import render
from blog.models import BlogPost

def blog(request):
    num_blog_posts = BlogPost.objects.all().count()

    context = {
        'num_blog_posts': num_blog_posts,
    }


    return render(request, 'blog.html', context=context)