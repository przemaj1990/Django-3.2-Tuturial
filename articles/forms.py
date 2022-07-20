from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
    #     #simple conditon to calidate data:
    #     if title.lower().strip() == "the office":
    #         raise forms.ValidationError('This title is taken')
    #     return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data', cleaned_data)
        # we can use validation here as well like in def clean_title
        # title = cleaned_data.get('title')
        # content = cleaned_data.get('content')
        # if title.lower().strip() == "the office":
        #     self.add_error('title', 'This title is taken')
        # if "office" in content or "office" in title.lower():
        #     self.add_error('content', 'Office in content')
        #     raise forms.ValidationError('Office is not allowed')
        return cleaned_data