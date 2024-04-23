# 46 - Complex Search using Django Q Lookups
# articles.models
def article_search_view(request):
    query_dict = request.GET
    try:
        query = int(query_dict.get('q'))
    except:
        query=None
    article_obj= None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {'object':article_obj}
    return render(request, 'articles/search.html', context=context)
    # ===============================
# Change this
def article_search_view(request):
    query_dict = request.GET
    try:
        query = int(query_dict.get('q'))
    except:
        query=None
    qs= Article.objects.all()
    if query is not None:
        qs = Article.objects.filter(title__icontains=query)
    context = {'object_list': qs}
    return render(request, 'articles/search.html', context=context)

    # search.html
    {% extends 'base.html' %}

    {% block content %}

    {% if object %}
    <h1>{{ object.title }}</h1>
    <p>{{ object.content }}</p>
    {% endif %}
    {% endblock %}
# Change this
{% extends 'base.html' %}

{% block content %}
    {% for object in object_list %}
        {% if object.title %}
            <h1>{{ object.title }}</h1>
            <p>{{ object.content }}</p>
            <p>{{ object.get_absolute_url }}</p>
        {% endif %}
    {% endfor %}
{% endblock %}
# Search Somtethint. It will serach in title only
# ============================================
{% extends 'base.html' %}

{% block content %}
    </ul>
        {% for object in object_list %}
            {% if object.title %}
            <li><a href="{{ object.get_absolute_url }}">{{ object.title }}</a></li>
            {% endif %}
        {% endfor %}
    </ul>
{% endblock %}
# Check this
# ============================================
# import Q from djang.db.model
def article_search_view(request):
    query = request.GET.get(q)
    qs= Article.objects.all()
    if query is not None:
        lookups= Q(title__icontains=query)
        qs = Article.objects.filter(lookups)
    context = {'object_list': qs}
    return render(request, 'articles/search.html', context=context)
# Check this with different search query
# ============================================
def article_search_view(request):
    query = request.GET.get(q)
    qs= Article.objects.all()
    if query is not None:
        lookups= Q(title__icontains=query) | Q(content__icontains=query)
        qs = Article.objects.filter(lookups)
    context = {'object_list': qs}
    return render(request, 'articles/search.html', context=context)