from django.http import HttpResponse
from django.template.loader import render_to_string
import random
from articles.models import Article

def home_view(request):

    article_obj = Article.objects.get(id=random.randint(1,4))
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object": article_obj,
        "id": article_obj.id,
        "title": article_obj.title,
        "content": article_obj.content,
    }
    
    HTML_STRING = render_to_string('home_view.html', context = context)


    return HttpResponse(HTML_STRING)