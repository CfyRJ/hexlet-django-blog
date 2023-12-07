from django.urls import path

from hexlet_django_blog.articles import views


urlpatterns = [
    # path('', views.index), view-function
    path('', views.IndexView.as_view(), name='article'), # view-class
    path('<str:tags>/<int:article_id>/', views.IndexView.as_view(), name='articles_tag_id')
]