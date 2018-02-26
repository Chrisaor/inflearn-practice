from django.http import HttpResponse
from django.shortcuts import render, redirect

from lotto.forms import PostForm
from lotto.models import GuessNumbers


def index(request):

    lottos = GuessNumbers.objects.all()
    context = {
        'lottos' : lottos,
    }
    return render(request, 'lotto/default.html', context)


def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()
            return redirect('index')
    else:
        form = PostForm()
        context = {
            'form': form,
        }
        return render(request, 'lotto/form.html', context)

def detail(request, pk):
    lotto = GuessNumbers.objects.get(pk=pk)
    context = {
        'lotto':lotto,
    }
    return render(request, 'lotto/detail.html', context)