from django.shortcuts import render, redirect
from .forms import wordform
from .models import Word
from django.http import Http404


# Create your views here.
def index(request):
    return render(request, 'index.html')

def wordin(request):
    if request.method == 'POST':
        form = wordform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = wordform()
    
    return render(request, 'addword.html', {'form' : form})

def wordshow(request):
    return render(request, 'wordshow.html', {'words' : Word.objects.all()} )

def wordmeaningshow(request, id):
    
    wordm = Word.objects.get(id=id)
    return render(request, 'modaltest.html', {'node':wordm})