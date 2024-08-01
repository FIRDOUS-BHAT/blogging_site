from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm


def blog_list(request):
	blogs = Blog.objects.all()
	return render(request, 'myapp/index.html', {'blogs': blogs})


def blog_detail(request, pk):
	blog = Blog.objects.get(pk=pk)
	return render(request, 'myapp/index2.html', {'blog': blog})


def edit_blog(request, pk):
	blog = get_object_or_404(Blog, pk=pk)
	if request.method == 'POST':
		form = BlogForm(request.POST, instance=blog)
		if form.is_valid():
			form.save()
			return redirect('blog_list')
	else:
		form = BlogForm(instance=blog)
	return render(request, 'myapp/edit.html', {'form': form})


def delete_blog(request, pk):
	blog = get_object_or_404(Blog, pk=pk)
	if request.method == 'POST':
		blog.delete()
		return redirect('blog_list')
	return render(request, 'myapp/delete.html', {'blog': blog})


def home(request):
	return HttpResponse('Hello, World!')
