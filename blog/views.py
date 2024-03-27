from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Post

# Create your views here.

def index(request):
    latest_blogs = Post.objects.order_by('-pub_date')[:2]
    context = {'latest_blogs': latest_blogs}
    return render(request, 'blog/index.html', context)

class BlogView(ListView):
    template_name = 'blog/list_blogs.html'
    context_object_name = 'latest_blogs'

    def get_queryset(self):
        '''Returns all the published blog posts'''
        return Post.objects.order_by('-pub_date')[:]

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def home(request):
    return render(request, 'index.html')