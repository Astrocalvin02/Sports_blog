from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Count, Q as models_Q
from .models import Post, SportCategory, Comment, UserProfile
from .forms import UserRegisterForm, UserProfileForm, PostForm, CommentForm, CategoryForm

# Home view
class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        return Post.objects.filter(status='published')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = SportCategory.objects.all()
        # Get popular posts without using Count on comments
        popular_posts = list(Post.objects.filter(status='published'))
        # Sort by active comment count in Python
        popular_posts.sort(key=lambda post: post.active_comments_count(), reverse=True)
        context['popular_posts'] = popular_posts[:3]
        return context

# Category view
class CategoryView(ListView):
    model = Post
    template_name = 'blog/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        self.category = get_object_or_404(SportCategory, slug=self.kwargs['slug'])
        return Post.objects.filter(category=self.category, status='published')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

# Post detail view
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all comments and filter in Python instead of at the database level
        all_comments = self.object.comments.all()
        context['comments'] = [comment for comment in all_comments if comment.active]
        context['comment_form'] = CommentForm()
        context['is_liked'] = False
        if self.request.user.is_authenticated:
            if self.object.likes.filter(id=self.request.user.id).exists():
                context['is_liked'] = True
        return context

# Create post view
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        # Generate slug from title
        from django.utils.text import slugify
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

# Update post view
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        # Update slug if title changed
        from django.utils.text import slugify
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete post view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('home')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# User registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

# User profile view
@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = UserProfileForm(instance=request.user.profile)
    
    user_posts = Post.objects.filter(author=request.user)
    
    context = {
        'profile_form': profile_form,
        'user_posts': user_posts
    }
    return render(request, 'blog/profile.html', context)

# Add comment to post
@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', slug=post.slug)
    return redirect('post_detail', slug=post.slug)

# Like post functionality
@login_required
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    # Check if request is AJAX (modern approach instead of deprecated request.is_ajax())
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'liked': liked, 'count': post.get_like_count()})
    
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# Search functionality
class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            # Use a simpler query structure that's better supported by Djongo
            return Post.objects.filter(
                status='published',
                title__icontains=query
            ) | Post.objects.filter(
                status='published',
                content__icontains=query
            )
        return Post.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['categories'] = SportCategory.objects.all()
        return context

# Legacy search function for backward compatibility
def search_posts(request):
    view = SearchResultsView.as_view()
    return view(request)
