from django.shortcuts import render
from django.core.paginator import Paginator
from.models import Post
# Create your views here.

def render_post3(request):
    posts = Post.objects.all().order_by('created_data')
    paginator = Paginator(posts, per_page=3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'pattern_alt.html', context)

def render_post5(request):
    posts = Post.objects.all().order_by('created_data')
    paginator = Paginator(posts, per_page=5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'pattern_alt.html', context)

def render_post10(request):
    posts = Post.objects.all().order_by('created_data')
    paginator = Paginator(posts, per_page=10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'pattern_alt.html', context)