from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


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

    def get(self, request, tags='', article_id='', *args, **kwargs):
            name = __package__

            return render(
                request,
                'articles/index.html',
                context={
                    'name': name,
                    'tags': tags,
                    'article_id': article_id,
                })