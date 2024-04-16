from django import forms

class ArticleForm(forms.Form):
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
