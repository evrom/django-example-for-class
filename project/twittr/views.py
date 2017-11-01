from django.shortcuts import render, redirect
from django.urls import reverse
# from django.http import HttpResponse

from twittr.forms import MessageForm
from twittr.models import Message


def my_view(request):
    form = MessageForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            Message.objects.create(
                message=form.cleaned_data['message'])
            return redirect(reverse('my_view'))
    messages = Message.objects.all()
    context = {
        'messages': messages,
        'form': form,
    }
    return render(request, 'my_template.html', context)
