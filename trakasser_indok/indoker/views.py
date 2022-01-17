from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Indoker
import re

# Create your views here.

def indoker(request, slug):
    indoker = Indoker.objects.get(slug=slug)
    messengerlink = indoker.facebooklink
    if "100" in messengerlink:
        messengerlink = re.sub(r'^.*?1', '1', indoker.facebooklink)
    else:
        while "/" in messengerlink:
            messengerlink = re.sub(r'^.*?/', '', messengerlink)
    messengerlink = f"https://www.messenger.com/t/{messengerlink}"
    return render(request, 'indoker/indoker.html', {
        'indoker': indoker,
        'messengerlink': messengerlink
    })

def indoker_list(request):
    indokere = Indoker.objects.all().order_by('etternavn')
    return render(request, 'indoker/indoker_list.html', { 'indokere': indokere})

@login_required()
def indoker_add(request):
    if request.method == 'POST':
        form = forms.CreateIndoker(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('indoker:list')
    else:
        form = forms.CreateIndoker()
    return render(request, 'indoker/add_indoker.html', {
        'form': form
    })