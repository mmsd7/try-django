from django.http import HttpResponse
import random
from articles.models import Article

def home_view(request):

    article_obj = Article.objects.get(id=random.randint(1,4))
    
    H_STRING = f"""
    <h1> Hello {article_obj.title}- : {article_obj.content} (ID: {article_obj.id})</h1>
    """
    P_STRING = f"""
    <p> Hello {article_obj.title}-  {article_obj.content}</p>
    """
    
    HTML_STRING = H_STRING + P_STRING


    return HttpResponse(HTML_STRING)