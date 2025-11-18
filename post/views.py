from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, login
from .models import Post
from .forms import PostForm
from django.views.generic import UpdateView
from .forms import RegisterForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def posts(request):
    posts = Post.objects.all().order_by("id")
    first_post = posts.first()
    trend_posts = Post.objects.filter(topic="Codding")

    p = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = p.get_page(page)

    context = {'posts':posts, 'first_post' : first_post, 'trend_posts':trend_posts}
    return render(request, 'blog/index.html', context)

def post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()
    previous_post = Post.objects.filter(id__lt=post.id).order_by('-id').first()

    context = {'post':post, 'next_post' : next_post, 'previous_post': previous_post}
    return render(request, 'post/details.html', context)


class PostsUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post/update.html'
    form_class = PostForm
    pk_url_kwarg = 'post_id'
    login_url = 'login'


def create(request):
    error = ''
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            error = "Форма заповнена не правильно"

    form = PostForm()

    data = {
        'form' : form,
        'error' : error,
    }
    return render(request, 'post/create.html', data)

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('posts')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {"form" : form})
