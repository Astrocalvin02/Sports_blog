from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class SportCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'Sport Categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_posts', args=[self.slug])

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(SportCategory, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    featured_image = models.ImageField(upload_to='posts/%Y/%m/%d/', blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    
    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])
    
    def get_like_count(self):
        return self.likes.count()
    
    def active_comments_count(self):
        return self.comments.filter(active=True).count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return f'Comment by {self.author.username} on {self.post}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    favorite_sports = models.ManyToManyField(SportCategory, blank=True, related_name='fans')
    
    def __str__(self):
        return f'{self.user.username} Profile'
