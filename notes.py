# 43 - Slugs in Dynamic Urls
# Working on trydjango app
# Here is the code we have in urls.py
urlpatterns = [
    path('', home_view),
    path('articles/', article_search_view),
    path('articles/create/', article_create_view),
    path('articles/<int:id>/', article_detail_view),
    path('admin/', admin.site.urls),
    path('login/', login_view ),
    path('logout/', logout_view),
    path('register/', register_view),
]

# Now let's make some changes
urlpatterns = [
    path('', home_view),
    path('articles/', article_search_view),
    path('articles/create/', article_create_view),
    path('articles/<slug:slug>/', article_detail_view),
    path('admin/', admin.site.urls),
    path('login/', login_view ),
    path('logout/', logout_view),
    path('register/', register_view),
]

# Our article.article_detail_views file is like below

def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context={
        'object': article_obj,
    }
    return render(request, 'articles/detail.html', context =  context)

# Now let's make some changes

def article_detail_view(request, slug=None): #MD
    article_obj = None
    if slug is not None:  #MD
        article_obj = Article.objects.get(id=slug)  #MD
    context={
        'object': article_obj,
    }
    return render(request, 'articles/detail.html', context =  context)
# Now let's make some changes

def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        article_obj = Article.objects.get(slug=slug)  #MD
    context={
        'object': article_obj,
    }
    return render(request, 'articles/detail.html', context =  context)

# +++++++++++++++++++++++
def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        article_obj = Article.objects.get(slug=slug)
    context={
        'object': article_obj,
    }
    return render(request, 'articles/detail.html', context =  context)

# TRY, It works fine!!

# +++++++++++++++++++++++
iport Http404 #NA
def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try: #NA
            article_obj = Article.objects.get(slug=slug)
        except:   #NA
            pass #NA
    context={
        'object': article_obj,
    }
    return render(request, 'articles/detail.html', context =  context)
# +++++++++++++++++++++++


def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try: 
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
    context={
        'object': article_obj,
    }
    return render(request, 'articles/detail.html', context =  context)

=============================================
def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try: 
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
    context={
        'object': article_obj,
    }
    return render(request, 'articles/detail.html', context =  context)

# home_view.html
{% extends 'base.html' %}

{% block content %}

<h1>{{ object.title }} ({{ object.id }})</h1>
<p> {{ object.content }} </p>


<ul>
    {% for x in object_list %}
        {% if x.title %}    
            <li> 
                <a href="/articles/{{ x.slug }}/"> {{ x.title }} - {{ x.content }} </a> #Modified
            </li>
        {% endif %}
    {% endfor %}


</ul>

{% endblock %}