from unicodedata import category

from django.shortcuts import get_object_or_404, render
from .models import Article, Category, SubCategory


def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    return render(request, "news/index.html", 
                  {"articles": articles, 
                   "categories": categories, 
                   "subcategories": subcategories})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    related_articles = Article.objects.filter(
        SubCategory=article.SubCategory
    ).exclude(
        id=article.id
    )

    return render(request, "news/detail.html", {
        "article": article,
        "categories": categories,
        "subcategories": subcategories,
        "related_articles": related_articles,
    })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)

    categories = Category.objects.all()
    subcategories = SubCategory.objects.filter(category=category)

    articles = Article.objects.filter(Category=category)

    return render(request, "news/category_detail.html", {
        "category": category,
        "categories": categories,
        "subcategories": subcategories,
        "articles": articles,
    })

def subcategory_detail(request, slug):
    subcategory = get_object_or_404(SubCategory, slug=slug)
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    articles = Article.objects.filter(SubCategory=subcategory)

    return render(request, "news/subcategory_detail.html", {
        "subcategory": subcategory,
        "categories": categories,
        "subcategories": subcategories,
        "articles": articles,
    })