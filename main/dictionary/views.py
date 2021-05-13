from django.shortcuts import render
from  .dictionary import Dictionary
from django.http import HttpResponseRedirect, HttpResponse

from . forms import NameForm

def index(request):
    # if this is a POST request we need ocess the form data
    if request.method == 'POST':
        # CREATE A FORM INSTARNCE AND POPULATE IT
        form = NameForm(request.POST)
        # CHECK VALIDIDTY
        if form.is_valid():
            word = form.cleaned_data['your_name']
            print(word)
            

            if Dictionary.get_verb(word):
                verb = Dictionary.get_verb(word)
            else:
                verb = False
            print(verb)

            if  Dictionary.get_noun(word):
                noun = Dictionary.get_noun(word)
            else:
                noun = False
            print(noun)

            synonyms = Dictionary.get_synonyms(word)
            print(synonyms)

            form = NameForm()

            context = {
                'word':word,
                'verb':verb,
                'noun':noun,
                'synonyms':synonyms,
                'form':form,
            }

            return render(request,'index.html', context)
    else:
        form = NameForm()

        context = {
            'form': form,
        }

    return render(request, 'index.html', context)
