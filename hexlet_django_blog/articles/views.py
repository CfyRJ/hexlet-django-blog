from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View

from hexlet_django_blog.articles.models import Article


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
