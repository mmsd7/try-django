from django.http import HttpResponse
import random

def home_view(request):
    name = 'Yousuf'
    number = random.randint(1, 5000)
    
    H_STRING = f"""
    <h1> Hello {name}- Here is the number: {number}</h1>
    """
    P_STRING = f"""
    <p> Hello {name}- Here is the number: {number}</p>
    """
    
    HTML_STRING = H_STRING + P_STRING


    return HttpResponse(HTML_STRING)