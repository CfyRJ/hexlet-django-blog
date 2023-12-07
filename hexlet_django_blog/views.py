from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import redirect

# View-function
# def index(request):
#     return render(request, 'index.html', context={
#         'who': 'World!',
#     })


def index_redirect(request):
    
    return redirect('articles_tag_id', tags='python', article_id=42)


# View-class
# class Index(TemplateView):
#     template_name = "index.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["who"] = 'World!'
#         return context


def about(request):
    return render(request, 'about.html')
