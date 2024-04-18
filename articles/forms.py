from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f'{title} has taken.')
        return data



class ArticleFormOld(forms.Form):
    title =  forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     title =  cleaned_data.get('title')
    #     if title.lower().strip() == "the office":
    #         raise forms.ValidationError('This title has been taken.')
    #     return title

    def clean(self):
        cleaned_data =  self.cleaned_data
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == 'the office':
            self.add_error('title', 'title is taken.')
        if 'office' in content or 'office' in title.lower():
            raise forms.ValidationError('OFFICE is not allowed.')  
        return cleaned_data
