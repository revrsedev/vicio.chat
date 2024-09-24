from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category, Tag

def post_list(request):
    posts = Post.objects.filter(status=True).order_by('-published_date')
    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'page_obj': page_obj, 'categories': categories})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories = Category.objects.all()
    return render(request, 'blog/post_detail.html', {'post': post, 'categories': categories})

def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.post_set.filter(status=True).order_by('-published_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'page_obj': page_obj, 'categories': categories, 'current_category': category})

def tag_view(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags__slug=slug, status=True).order_by('-published_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'page_obj': page_obj, 'categories': categories, 'current_tag': tag})
