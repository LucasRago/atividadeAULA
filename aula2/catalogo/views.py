from django.shortcuts import render
import requests


def pagina_inicial(request):
    resposta = requests.get("https://omdbapi.com/?apikey=38b4b85b&s=Harry-Potter&type=movie")
    dados_api = resposta.json()
    filmes = dados_api["Search"]
    contexto = {
        "filmes": filmes
    }
    return render(request, "pagina_inicial.html", contexto)
