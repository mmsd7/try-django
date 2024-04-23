# 45 - Django URLs Reverse

# ====================================
# Add name
urlpatterns = [
    path('', home_view),
    path('articles/', article_search_view),
    path('articles/create/', article_create_view, name="article-create"),
    path('articles/<slug:slug>/', article_detail_view, name="article-detail"),
    path('admin/', admin.site.urls),
    path('login/', login_view ),
    path('logout/', logout_view),
    path('register/', register_view),
]

# Import reverse in aritcles.modles
# articles.models.py
    def get_absolute_url(self):
        # return f'/articles/{self.slug}/' #MD
        return reverse(article-create) #ADD
# Check! It's not a dynamic URL


# ====================================
# articles.models.py
    def get_absolute_url(self):
        # return f'/articles/{self.slug}/' 
        return reverse(article-detail)
# Check! It should display no arguments
# ====================================
# articles.models.py
    def get_absolute_url(self):
        # return f'/articles/{self.slug}/' 
        return reverse(article-detail, kwargs={"slug":self.slug}) #md
        # (this KYE "SLUG" is related to URL_Patterns)
# Check! It will works
# ====================================
# home-view.html
{% extends 'base.html' %}
{% block content %}
<h1>{{ object.title }} ({{ object.id }})</h1>
<p> {{ object.content }} </p>
<ul>
    {% for x in object_list %}
        {% if x.title %}    
            <li> 
                <a href="{{ x.get_absolute_url }}"> {{ x.title }} - {{ x.content }} </a> 
            </li>
            </li>
        {% endif %}
    {% endfor %}
</ul>
{% endblock %}
# ====================================
# Let's change this
{% extends 'base.html' %}
{% block content %}
<h1>{{ object.title }} ({{ object.id }})</h1>
<p> {{ object.content }} </p>
<ul>
    {% for x in object_list %}
        {% if x.title %}    
            <li> 
                <a href="{% url 'article-create' %}"> {{ x.title }} - {{ x.content }} </a> #md 
            </li>
            </li>
        {% endif %}
    {% endfor %}
</ul>
{% endblock %}
# Check! It will works
# ====================================
{% extends 'base.html' %}
{% block content %}
<h1>{{ object.title }} ({{ object.id }})</h1>
<p> {{ object.content }} </p>
<a href="{% url 'article-create' %}">Create Article</a> #add
<a href="{% url 'article-detail' slug=hello-world %}">Hello World Article</a> #add
<ul>
    {% for x in object_list %}
        {% if x.title %}    
            <li> 
                <a href="{% url 'article-detail' slug=x.slug %}"> {{ x.title }} - {{ x.content }} </a> #md 
            </li>
            </li>
        {% endif %}
    {% endfor %}
</ul>
{% endblock %}
# Check! It will works
# ====================================
# THIS IS NOT A GOOD PRACTICE. Rather do the following
# ===================================
{% extends 'base.html' %}
{% block content %}
<h1>{{ object.title }} ({{ object.id }})</h1>
<p> {{ object.content }} </p>
<a href="{% url 'article-create' %}">Create Article</a>
<a href="{% url 'article-detail' 'slug=hello-world' %}">Hello World Article</a> 
<ul>
    {% for x in object_list %}
        {% if x.title %}    
            <li> 
                <a href="{{ x.get_absolute_url }}> {{ x.title }} - {{ x.content }} </a> #md 
            </li>
            </li>
        {% endif %}
    {% endfor %}
</ul>
{% endblock %}
# Check. It should work
# ====================================
# Navigate to article_create_view
# Import redirect
@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form' :  form
    }
    
    if form.is_valid():
        article_obj =  form.save()
        context['form'] = ArticleForm()
        redirect(article_obj.get_absolute_url()) #NA
        # redirect('article-datail', slug=article_obj.slug) #NA, It also works
    return render (request, 'articles/create.html', context=context)
# Create an article and try
# ====================================

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form' :  form
    }
    
    if form.is_valid():
        article_obj =  form.save()
        context['form'] = ArticleForm()
        redirect(article_obj.get_absolute_url())
        # redirect(article_obj.get_absolute_url()) #NA
        # redirect('article-datail', slug=article_obj.slug) #NA, It also works
    return render (request, 'articles/create.html', context=context)