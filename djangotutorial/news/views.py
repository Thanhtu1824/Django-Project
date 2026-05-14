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
    return render(request, "news/detail.html", {"article": article})


