from unicodedata import category

from django.shortcuts import render
from .models import Article, Category, SubCategory


def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    return render(request, "news/index.html", 
                  {"articles": articles, 
                   "categories": categories, 
                   "subcategories": subcategories})


