from django.shortcuts import render
import urllib
import json
# Create your views here.
def dictionary(request) :
  
    word = request.POST.get('word')
    if(request.method == 'POST') :
        data_from_api = urllib.request.urlopen('https://api.dictionaryapi.dev/api/v2/entries/en/'+word).read()
        data = json.loads(data_from_api) 
        infos = {
           'word':data[0]['word'],
           'definition' : data[0]['meanings'][0]['definitions'][0]['definition'],
           'phonetic':data[0]['phonetic'],
           'phonetics':data[0]['phonetics'][0]['audio'],
           'origin':data[0]['origin'],
           'synonyms' : data[0]['meanings'][0]['definitions'][0]['synonyms'],
           'antonyms' : data[0]['meanings'][0]['definitions'][0]['antonyms'],
           'partOfSpeech' : data[0]['meanings'][0]['partOfSpeech'],
           
       }
    else :
          infos = { }   
       
    return render(request,'dictionaryapp/home.html',{'infos':infos})

