from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from postApp import forms
from .models import Post, Category, Publisher, Author


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'all.html', {'posts': posts})


def add_new(request):
    default()
    if request.method == 'POST':
        post = Post()
        is_publish = request.POST.get('is_publish')
        if is_publish:
            post.header = request.POST.get('header')
            post.content = request.POST.get('content')
            post.date = request.POST.get('date')
            post.category_id = request.POST.get('category')
            post.author_id = request.POST.get('author')
            post.publisher_id = request.POST.get('publisher')
            post.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('<h2>Post not published</h2>')
    else:
        post = forms.PostForm()
        categories = Category.objects.all()
        authors = Author.objects.all()
        publishers = Publisher.objects.all()
        return render(request, 'add_new.html',
                      {'form': post, 'categories': categories, 'authors': authors, 'publishers': publishers})


def edit(request, id):
    try:
        post = Post.objects.get(id=id)
        if request.method == 'POST':
            post.header = request.POST.get('header')
            post.content = request.POST.get('content')
            post.date = request.POST.get('date')
            post.category_id = request.POST.get('category')
            post.author_id = request.POST.get('author')
            post.publisher_id = request.POST.get('publisher')
            post.save()
            return HttpResponseRedirect('/')
        else:
            categories = Category.objects.all()
            authors = Author.objects.all()
            publishers = Publisher.objects.all()
            return render(request, 'edit.html',
                          {'post': post, 'categories': categories, 'authors': authors, 'publishers': publishers})
    except post.DoesNotExist:
        return HttpResponseNotFound('<h2>Post id not found</h2>')


def delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect('/')
    except post.DoesNotExist:
        return HttpResponseNotFound('<h2>Post id not found</h2>')


def default():
    if Category.objects.all().count() == 0:
        Category.objects.create(name='Games')
        Category.objects.create(name='Culture')
        Category.objects.create(name='School subjects')
    if Author.objects.all().count() == 0:
        Author.objects.create(name='Jhon', age=42)
        Author.objects.create(name='Aleksandr', age=30)
    if Publisher.objects.all().count() == 0:
        Publisher.objects.create(name='OAO "Good books"', boss='Ivanov Ivan Jovanovich')
