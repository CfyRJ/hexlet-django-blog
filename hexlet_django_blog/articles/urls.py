from django.urls import path

from hexlet_django_blog.articles.views import IndexView


urlpatterns = [
    # path('', views.index), view-function
    path('', IndexView.as_view(), name='article_index'), # view-class
    path('<str:tags>/<int:article_id>/', IndexView.as_view(), name='articles_tag_id')
]