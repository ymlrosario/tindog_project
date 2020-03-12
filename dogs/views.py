from django.shortcuts import render
from .models import Comment

def index(request):
    comments = Comment.objects.all()
    context = {
        'comments': comments
    }

    return render(request, 'dogs/index.html', context)

def about(request):
    return render(request, 'dogs/about.html')
