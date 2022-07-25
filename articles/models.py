from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    upadted = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False, auto_now=False, default=timezone.now, null=True, blank=True)

    def save(self, *arg, **kwargs):
        # right here we execute something like:
        # obj = Article.objects.get(id=1)
        # obj.save()
        # so before this save we would like to add sluggify and change title
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*arg, **kwargs)