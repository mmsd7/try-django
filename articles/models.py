import random
from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.utils import timezone
from django.utils.text import slugify

from .utils import slugify_instance_title

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, null = True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    publish = models.DateField(auto_now_add = False, auto_now = False, null=True, blank = True)

    def get_absolute_url(self):
        # return f'/articles/{self.slug}/'
        return reverse('article-detail', kwargs={"slug":self.slug})

    def save(self, *args, **kwargs):
        #obj = Article.objects.get(id=5)
        #set something
        # if self.slug is None:
        #     self.slug = slugify(self.title) 
        super().save(*args, **kwargs)
        #obj.save()
        #Do anothe rsomething

def article_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    if instance.slug is None:
        slugify_instance_title(instance, save=False)
    

pre_save.connect(article_pre_save, sender = Article)

def article_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    if created:
        slugify_instance_title(instance, save=True)

    
post_save.connect(article_post_save, sender = Article)