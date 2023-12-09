from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib import messages

from hexlet_django_blog.articles.models import Article
from hexlet_django_blog.articles.forms import ArticleForm


# Create your views here.
# View-function
# def index(request):
#     name = __package__

#     return render(
#         request,
#         'articles/index.html',
#         context={
#             'name': name
#         })


# View-class
class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]

        return render(
            request,
            'articles/index.html',
            context={
                'articles': articles
            }
        )


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])

        return render(
            request,
            'articles/show.html',
            context={
                'article': article
            }
        )


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(
            request,
            'articles/create.html',
            context={
                'form': form,
            }
        )

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Article added successfully')
            form.save()
            return redirect('article_index')

        messages.add_message(request, messages.ERROR, 'Error')

        return render(
            request,
            'articles/create.html',
            context={
                'form': form,
            }
        )


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)

        return render(
            request,
            'articles/update.html',
            context={
                'article_id': article_id,
                'form': form,
            }
        )

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Article added successfully')
            return redirect('article_index')
        
        messages.add_message(request, messages.ERROR, 'Error')

        return render(
            request,
            'articles/update.html',
            context={
                'article_id': article_id,
                'form': form,
            }
        )


class ArticleFormDeleteView(View):
    def post(self, request, *aargs, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            messages.add_message(request, messages.SUCCESS, 'Article deleted successfully')
            article.delete()

        return redirect('article_index')
