from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
import datetime
from .models import Blog, Comments
from .forms import CommentForm

def index(request):
    blogs = Blog.objects.all()
    response = {'blog': blogs}
    return render(request,'index.html',response)

def blog_detail(request,id):
    response={
        'blog':get_object_or_404(Blog,pk=id),
        'comment':get_object_or_404(Blog,pk=id).comments.all()
    }
    return render(request, 'detail.html', response)

@login_required(login_url='account/login')
def create_comment(request,id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comments = form.save(commit=False)
            comments.author = request.user
            comments.blog = get_object_or_404(Blog,pk=id)
            comments.save()
            return redirect('/blog/detail/'+str(id))
    else:
        form = CommentForm()

    context = {
        'form': form,
    }
    return render(request, 'comment.html', context)


@login_required(login_url='account/login')
def edit_comment(request, id):
    comment = get_object_or_404(Comments, pk=id)
    if request.user != comment.author:
        return redirect('/blog/detail/'+str(comment.blog.id))

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid:
            comments = form.save(commit=False)
            comments.added = datetime.datetime.now()
            comments.save()
            return redirect('/blog/detail/'+str(comment.blog.id))
    else:
        form = CommentForm(instance=comment)
    context={
        'form':form
    }
    return render(request, 'comment.html', context)


@login_required(login_url='account/login')
def delete_comment(request, id):
    comment = get_object_or_404(Comments, pk=id)
    if request.user != comment.author:
        redirect('/blog/detail/'+str(comment.blog.id))

    comment.delete()
    return redirect('/blog/detail/'+str(comment.blog.id))
