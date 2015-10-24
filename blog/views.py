from django.shortcuts import render, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Article
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
# Create your views here.

# def home(request):
#     post_list = Article.objects.all()
#     html = '<p>hello world</p>'
#     return render_to_response('home.html', {"post_list": post_list})
#     # return HttpResponse(html)
#
#
# def detail(request, id):
#     try:
#         post = Article.objects.get(id=str(id))
#     except Article.DoesNotExist:
#         raise Http404
#     return render_to_response('post.html', locals())

class Detail(DetailView):
    template_name = 'post.html'
    model = Article
    context_object_name = 'post'
    slug_field = 'id'
    def get_context_data(self, **kwargs):
        id = self.kwargs.get('slug', '')
        print id
        kwargs['post'] = Article.objects.get(id=str(id))
        return super(Detail, self).get_context_data(**kwargs)



class Home(ListView):
    template_name = 'home.html'
    model = Article
    context_object_name = 'post_list'


