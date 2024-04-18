# Model Form for Article Model

# Rename the class ArticleForm() to ArticleFormOld()
# Create the new following class

class ArticleForm(form.ModelForm):
    class meta:
        model = Article
        fields = ['title', 'content']

# Run the articles/create url. It will work fine.
# Now open the views.py file and make changes like shown below
# This is the existing code
@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form' :  form
    }
    if form.is_valid():
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        article_obj = Article.objects.create(title= title, content=content)
        context['object'] = article_obj
        context['created'] = True
    return render (request, 'articles/create.html', context=context)

# Let's modify this
@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form' :  form
    }
    if form.is_valid():
        article_obj = aform.save() #Add this line and comment out the lines below
        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')
        # article_obj = Article.objects.create(title= title, content=content)
        context['object'] = article_obj
        context['created'] = True
    return render (request, 'articles/create.html', context=context)
# Check the code. It should work fine.

# Now change the context. Otherwise the form doesn't get clean and make repeated post if tried.
@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form' :  form
    }
    if form.is_valid():
        article_obj = aform.save()
        context['form'] = ArticleForm() # Add this line
        # context['object'] = article_obj #delete this
        # context['created'] = True #delete this
    return render (request, 'articles/create.html', context=context)

#check

class ArticleForm(form.ModelForm):
    class meta:
        model = Article
        fields = ['title', 'content']

        def clean(self):
            data =  self.cleaned_data
            title = data.get('title')
            qs =  Article.objects.filter(title__icontains=title)
            if qs.exist():
                self.add_error("title", f"{title} is already taken.")
            return data
# Check