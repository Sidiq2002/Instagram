from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth import logout
from .models import Post 
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth import login

@login_required
def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'feed.html', {'posts': posts})


# def feed(request):
#     posts = Post.objects.all().order_by('-created_at')  # shows all users' posts
#     return render(request, 'feed.html', {'posts': posts})
# def feed(request):
#     posts = Post.objects.all().order_by('-created_at')
#     return render(request, 'feed.html', {'posts': posts})

@login_required
def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'upload.html', {'form': form})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('feed')

@login_required
def comment_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
    return redirect('feed')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')




def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user).order_by('-created_at')
    return render(request, 'profile.html', {'profile_user': user, 'posts': posts})



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})




# from django.shortcuts import render, redirect
# from .forms import SignUpForm

# def signup_view(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})
