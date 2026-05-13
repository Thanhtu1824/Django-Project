from django.contrib import admin

from news.define import ADMIN_HEADER_NAME

# Register your models here.
from .models import Category, Feed, SubCategory
from .models import Article


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'layout', 'is_homepage', 'ordering',)
    # prepopulated_fields = {'slug': ('name',)}

    list_filter = ["is_homepage", "status", "layout"]
    radio_fields = {"is_homepage": admin.HORIZONTAL}
    search_fields = ["name"]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'special', 'public_date', 'Category', 'SubCategory',)
    # prepopulated_fields = {'slug': ('name',)}
    radio_fields = {"special": admin.HORIZONTAL}
    list_filter = ["status", "special", "Category", "SubCategory"]
    search_fields = ["name"]


class FeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'link', 'status', 'ordering',)
    # prepopulated_fields = {'slug': ('name',)}

    list_filter = ["status"]
    search_fields = ["name"]

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'status', 'ordering', 'category',)
    # prepopulated_fields = {'slug': ('name',)}

    list_filter = ["status"]
    search_fields = ["name", "category__name"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Feed, FeedAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)

admin.site.site_header = ADMIN_HEADER_NAME
