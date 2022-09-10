from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput


class CommentForm(forms.Form):
    name = forms.CharField(max_length=20, min_length=1, label='Ник (до 20 символов) ',
                           widget=forms.TextInput(attrs={"class":"form-control"}))
    content = forms.CharField(min_length=3, label='Текст ',
                              widget=forms.Textarea(attrs={"class":"form-control", "rows":7}))
    captcha=CaptchaField()

