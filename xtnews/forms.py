import wtforms as forms

class NewsForm(forms.Form):
    title = forms.TextField('title', [forms.validators.required()])
    text = forms.TextField('text', [forms.validators.required()])
