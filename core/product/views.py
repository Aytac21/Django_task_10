from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm


def list_view(request):
    context = {
        "blogs": Blog.objects.all(),
    }
    return render(request, "list.html", context)


def create_view(request):

    form = BlogForm()

    if request.method == "POST":
        form = BlogForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("blog:list")

    context = {
        "form": form,
    }
    return render(request, "create.html", context)


def update_blog_view(request, id):
    blog = get_object_or_404(Blog, id=id)
    form = BlogForm(instance=blog)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()

            return redirect("blog:list")
    context = {
        "form": form
    }
    return render(request, "update.html", context)


def detail_view(request, id):
    blogs = Blog.objects.get(id=id)
    context = {
        "id": id,
        "blogs": blogs
    }
    return render(request, "detail.html", context)
