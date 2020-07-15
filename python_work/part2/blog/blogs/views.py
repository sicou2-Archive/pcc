from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import PostForm

# Create your views here.


def index(request):
    """The home page for the Blog."""
    blogs = BlogPost.objects.order_by('date_added')

    context = {
        'blogs': blogs,
    }
    return render(request, 'blogs/index.html', context)


def new_post(request):
    """Add a new blog post."""
    if request.method != 'POST':
        # No data submitted, process data.
        form = PostForm()
    else:
        # POST data submitted, process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


def edit_post(request, entry_id):
    """Edit a blog post."""
    post = BlogPost.objects.get(id=entry_id)

    if request.method != 'POST':
        # No data submitted, display current entry to edit.
        form = PostForm(instance=post)
    else:
        # POST data submitted, process data.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
