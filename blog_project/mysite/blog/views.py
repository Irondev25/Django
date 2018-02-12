from django.shortcuts import render
from django.views import generic
from .models import Post
from blog.forms import PostForm, CommentForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here

class AboutView(generic.TemplateView):
    template_name = 'about.html'

class PostListView(generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(
            published_date__lte=timezone.now()
            ).order_by('-published_date')

class PostDetailView(generic.DetailView):
    model = Post


class CreatePostView(generic.CreateView, LoginRequiredMixin):
    #attributes required for LoginRequiredMixin
    login_url = '/login/'     #attribute from LoginRequiredMixin, this redirect them to login page
    redirect_field_name = 'blog/post_detail.html' #after login verification it redirect to post_detail.html page

    #this is for CreateView
    model = Post
    form_class = PostForm

class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    #attributes required for LoginRequiredMixin
    # attribute from LoginRequiredMixin, this redirect them to login page
    login_url = '/login/'
    # after login verification it redirect to post_detail.html page
    redirect_field_name = 'blog/post_detail.html'

    #this is for CreateView
    model = Post
    form_class = PostForm

class PostDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True)/
        .order_by('created_date')