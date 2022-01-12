from .models import Post
from django.shortcuts import render
from django.shortcuts import redirect


def view_blog_list(request):
    #blog_list = Post.objects.all()
    blog_list = Post.objects.order_by("-created_at")
    data = {"post_list": blog_list}
    return render(request, 'blog/view_blog_list.html', data)

def add_blog_form(request):
    return render(request, 'blog/add_blog_form.html')

def add_blog(request):
    input1 = request.POST.get("title")
    input2 = request.POST.get("writer")
    input3 = request.POST.get("content")

    p = Post(title = input1, writer = input2, content = input3)
    p.save()

    return redirect("/")

def view_blog(request, blog_id):
    b = Post.objects.get(id=blog_id)
    data = {"blog": b}
    return render(request, 'blog/view_blog.html', data)

def edit_blog_form(request, blog_id):
    b = Post.objects.get(id=blog_id)
    data = {"blog": b}
    return render(request, 'blog/edit_blog_form.html', data)