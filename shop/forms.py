from django import forms



class ContactForm(forms.Form):
    subject = forms.CharField(max_length=20, min_length=1, label='Контакт для связи',
                           widget=forms.TextInput(attrs={"class":"form-control"}))
    content = forms.CharField(min_length=3, label='Комментарии к заказываемому товара',
                              widget=forms.Textarea(attrs={"class":"form-control", "rows":5}))