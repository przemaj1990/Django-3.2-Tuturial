from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from .utils import sluggify_instance_title

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    upadted = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False, auto_now=False, default=timezone.now, null=True, blank=True)

    def save(self, *args, **kwargs):
        # right here we execute something like:
        # obj = Article.objects.get(id=1)
        # obj.save()
        # so before this save we would like to add sluggify and change title
        # but we will do this in pre_save
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)

# after every save pre-save will connect to def article_pre_save
def article_pre_save(sender, instance, *arg, **kwargs):
    # print(pre_save)
    # print(arg, kwargs)
    # print(sender, instance)
    # example how to modify something before save
    if instance.slug is None:
    #     slug = slugify(instance.title)
    #     instance.slug = slug
        sluggify_instance_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Article)

def article_post_save(sender, instance, created, *arg, **kwargs):
    # print(post_save)
    # print(arg, kwargs)
    # example how to modify something after save
    if created:
        # instance.slug = 'this is my slug'
        # slug = slugify(instance.title)
        # instance.slug = slug
        # instance.save()
        sluggify_instance_title(instance, save=True)

post_save.connect(article_post_save, sender=Article)