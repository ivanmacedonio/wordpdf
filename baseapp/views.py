from django.shortcuts import render
from .models import WordHistory, FileModel



def receive_data_get(self, request):  # Sin magic
    if request.method == "GET":
        word = request.GET.get("word")
        line = request.GET.get("line")
        filedata = request.FILES.get("filedata")
        user = request.user

    if word:
        word_instance = WordHistory(word=word, user=user)
        word_instance.save()
        file_instance = FileModel(filedata=filedata, line=line, word=word, user=user)
        file_instance.save()
    else:
        return 0
