from django.shortcuts import render
from .models import WordHistory, FileModel
from django.http import JsonResponse
from django.core import serializers
import json
from django.http import HttpResponseBadRequest


class DataTypeError(Exception):
    def __init__(self, message):
        self.message = message


def receive_data_get(self, request):  # Sin magic
    try:
        if request.method == "GET":
            word = request.GET.get("word")
            line = request.GET.get("line")
            filedata = request.FILES.get("filedata")
            user = request.user

        if word:
            word_instance = WordHistory(word=word, user=user)
            word_instance.save()
            file_instance = FileModel(
                filedata=filedata, line=line, word=word, user=user
            )
            file_instance.save()
        else:
            raise DataTypeError("Tipo de dato invalido")
    except DataTypeError as e:
        return HttpResponseBadRequest(e.message)


def obtain_word(self, request):  # retorna el historial de palabras visitadas
    query = WordHistory.objects.all()
    json_data = serializers.serialize("json", query)
    return JsonResponse(json_data, safe=False)
