from django.test import TestCase
from django.utils.text import slugify

# Create your tests here.
from .models import Article
from .utils import sluggify_instance_title
class ArticleTestCase(TestCase):

    # as test are not run on prod database, we need to setup everything before 
    # for test run on test db
    def setUp(self):
        self.number_of_articles = 50
        for i in range(0, self.number_of_articles):
            Article.objects.create(title='hello world', content='something else')

    def test_querryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_querryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), self.number_of_articles)

    def test_hello_world_slug(self):
        obj = Article.objects.all().order_by('id').first()
        title = obj.title
        slug = obj.slug
        slugified_title = slugify(title)
        self.assertEqual(slug, slugified_title)

    def test_hello_world_not_slug(self):
        qs = Article.objects.exclude(slug__iexact='hello-world')
        for obj in qs:
            title = obj.title
            slug = obj.slug
            slugified_title = slugify(title)
            self.assertNotEqual(slug, slugified_title)

    def test_sluggify_instance_title(self):
        obj = Article.objects.all().last()
        new_slugs = []
        for i in range(0, 25):
            instance = sluggify_instance_title(obj, save=False)
            new_slugs.append(instance.slug)
        #set remove duplicates
        unique_slugs = list(set(new_slugs))
        self.assertEqual(len(new_slugs), len(unique_slugs))

    def test_slugify_instance_title_redux(self):
        slug_list = Article.objects.all().values_list('slug', flat=True)
        unique_slug_list = list(set(slug_list))
        self.assertEqual(len(slug_list), len(unique_slug_list))
