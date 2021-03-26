from django.shortcuts import render, redirect
from .models import Article
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articles/new_article.html'
    fields = ('title', 'author', 'body')
# ---- C R E A T E   B L O G


# ---- A L L   A R T I C L E S
class ArticleListView(ListView):
    model = Article
    template_name = "articles/all_articles.html"
    context_object_name = "articles"


# ---- O N E   A R T I C L E
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/one_article.html'


# ---- U P D A T E   A R T I C L E
class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'articles/edit_article.html'
    fields = ('title', 'body')


# ---- D E L E T E   A R T I C L E
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/delete_article.html'
    success_url = reverse_lazy('all_articles')
