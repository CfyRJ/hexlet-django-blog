from django.urls import path

from hexlet_django_blog.articles.views import (IndexView,
                                               ArticleView,
                                               ArticleFormCreateView
                                               )


urlpatterns = [
    # path('', views.index), view-function
    path('', IndexView.as_view(), name='article_index'), # view-class
    path('<int:id>/', ArticleView.as_view(), name='articles_view'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]
