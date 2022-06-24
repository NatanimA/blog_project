from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog.models import Post,Comments
from blog.forms import PostForm,CommentsForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,
                                    DetailView,CreateView,UpdateView,
                                    DeleteView)

# Create your views here.


class AboutView(TemplateView):
    template_name='blog/about.html'

class PostListView(ListView):
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail'
    form_class=PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail'
    form_class=PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    model = Post
    success_url= reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='blog/post-list.html'
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')


##################################
# Comments
##############################

@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method== 'POST':
        form=CommentsForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=CommentsForm()
    return render(request,'blog/comment_form.html',{'form':form})





@login_required
def comments_approve(request,pk):
    comments=get_object_or_404(Comments,pk=pk)
    comments.approve()
    return redirect('post_detail',pk=comments.post.pk)

@login_required
def comments_remove(request,pk):
    comments=get_object_or_404(Comments,pk=pk)
    post_pk =comments.post.pk
    comments.delete()
    return redirect('post_detail',pk=post_pk)

def posts_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
