from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from .utils import sluggify_instance_title
from django.urls import reverse
from django.db.models import Q
from django.conf import settings

User = settings.AUTH_USER_MODEL

class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups) 

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

    # def search(self, query=None):
    #     if query is None or query == "":
    #         self.get_queryset().none() #the same as Article.objects.none()
    #     lookups = Q(title__icontains=query) | Q(content__icontains=query)
    #     return self.get_queryset().filter(lookups)


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    upadted = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False, auto_now=False, default=timezone.now, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    objects=ArticleManager()

    def get_absolute_url(self):
        # return f"/articles/{self.slug}"
        return reverse('article-detail', kwargs={"slug": self.slug})

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