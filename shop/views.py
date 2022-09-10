from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Shop
from django.core.mail import send_mail
from .forms import ContactForm

def index_shop(request):
    shop = Shop.objects.all()
    context = {'content': shop,
               'title': 'Каталог товаров'}
    return render(request, 'shop/index_shop.html', context)

def mail(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            mail=send_mail(form.cleaned_data['subject'],
                      form.cleaned_data['content'],'evgen.guk@ukr.net',['evgen.guk@yandex.ru'],
                      fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('mail')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form=ContactForm()
    return render(request,'shop/mail.html',{"form":form})

