
import os, uuid

from slugify import slugify
from django.db import models
from tinymce.models import HTMLField

from news.define import APP_VALUE_LAYOUT_CHOIECES, APP_VALUE_LAYOUT_DEFAULT, APP_VALUE_STATUS_CHOICES, APP_VALUE_STATUS_DEFAULT, TABLE_ARTICLE_SHOW, TABLE_ARTICLES_SHOW, TABLE_CATEGORIES_SHOW, TABLE_CATEGORY_SHOW, TABLE_FEED_SHOW, TABLE_FEEDS_SHOW

BOOLEAN_CHOICES = (
    (True, 'Có'),
    (False, 'Không'),
)

def get_file_path (instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('news/images/articles/', filename)

# Create your models here.
class Category(models.Model):

    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField( unique=True, max_length=100, blank=True)
    is_homepage = models.BooleanField(choices=BOOLEAN_CHOICES, default=False)
    layout = models.CharField(max_length=10, choices=APP_VALUE_LAYOUT_CHOIECES, default=APP_VALUE_LAYOUT_DEFAULT)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name = TABLE_CATEGORY_SHOW
        verbose_name_plural = TABLE_CATEGORIES_SHOW

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) 
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Article(models.Model):

    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField( unique=True, max_length=100, blank=True)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default='draft')
    ordering = models.IntegerField(default=0)
    summary = HTMLField()
    content = HTMLField()
    special = models.BooleanField(choices=BOOLEAN_CHOICES, default=False)
    public_date = models.DateTimeField()
    image = models.ImageField(upload_to=get_file_path)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    SubCategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = TABLE_ARTICLE_SHOW
        verbose_name_plural = TABLE_ARTICLES_SHOW

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Feed(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField( unique=True, max_length=100, blank=True)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    link = models.URLField(unique=True, max_length=250)

    class Meta:
        verbose_name = TABLE_FEED_SHOW
        verbose_name_plural = TABLE_FEEDS_SHOW

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Feed, self).save(*args, **kwargs)


    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField( unique=True, max_length=100, blank=True)
    is_homepage = models.BooleanField(choices=BOOLEAN_CHOICES, default=False)
    layout = models.CharField(max_length=10, choices=APP_VALUE_LAYOUT_CHOIECES, default=APP_VALUE_LAYOUT_DEFAULT)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) 
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name