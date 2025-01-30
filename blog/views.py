from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.

#vista para listar los post
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})


#vista para crear nuevos post
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
            form = PostForm()

    return render(request, 'blog/post_create.html', {'form':form})

def post_delete(request, post_id):
     post = get_object_or_404(Post, id=post_id)
     if request.method == 'POST':
          post.delete()
          return redirect('post_list')
     return render(request, 'blog/post_confirm_delete.html', {'post': post})


def post_edit(request, post_id):
     post = get_object_or_404(Post, id=post_id)
     if request.method == 'POST':
          form = PostForm(request.POST, instance=post)
          if form.is_valid():
               form.save()
               return redirect('post_list')
     else:
        form = PostForm(instance=post)
        
     return render(request, 'blog/post_edit.html', {'form': form})