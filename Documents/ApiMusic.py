from flask import Flask
import requests
import json
import heapq

app = Flask(__name__)

link = 'https://mixer-mp3-default-rtdb.firebaseio.com/'

# criando um estilo com post
#dados = {
#    '1': "AC_DC - Thunderstruck (Official Video) (MP3_128K).mp3"]
#}
#requisicao = requests.post(
#f'{link}/musicas/.json',
#data=json.dumps(dados))  #passando um dicionario em formato json

#json.dumps pega um texto e transforma num formato json
#print(requisicao)
#print(requisicao.text)

#editando o estilo com patch
#requisicao = requests.patch(
#f'{link}/musicas/-NI07aBVl9jU1FK1QN_C/rock/.json',
#data=json.dumps(dados))

#for id_musica in dic_requisicao:
#    musica = dic_requisicao[id_musica]['rock']
#    if musica == "music/AC_DC - Thunderstruck (Official Video)           (MP3_128K).mp3":
#       print(id_musica)

#deletar com delete
#requisicao = requests.delete(f'{link}/musicas/{id_musica}/.json')
#print(requisicao)
#print(requisicao.text)


@app.route('/')
def homepage():
    list = []
    #pegar dados com get
    requisicao = requests.get(
        f'{link}/.json'
    )  #colocando "&orderby" ao lado do .json, os dados retornam em ordem
    dic_requisicao = requisicao.json()
    print(dic_requisicao)
    for estilo in dic_requisicao['musicas']['-NI07aBVl9jU1FK1QN_C']:
        heapq.heapify(list)
        heapq.heappush(list, estilo)

    print(list)
    return list


@app.route('/rock')
def rock():
    list = []
    #pegar dados com get
    requisicao = requests.get(
        f'{link}/.json'
    )  #colocando "&orderby" ao lado do .json, os dados retornam em ordem
    dic_requisicao = requisicao.json()
    print(dic_requisicao)
    for musica in dic_requisicao['musicas']['-NI07aBVl9jU1FK1QN_C']['rock']:
        heapq.heapify(list)
        heapq.heappush(list, musica)

    print(list)
    return list


@app.route('/sertanejo')
def sertanejo():
    list = []
    #pegar dados com get
    requisicao = requests.get(
        f'{link}/.json'
    )  #colocando "&orderby" ao lado do .json, os dados retornam em ordem
    dic_requisicao = requisicao.json()
    print(dic_requisicao)
    for musica in dic_requisicao['musicas']['-NI07aBVl9jU1FK1QN_C'][
            'sertanejo']:
        heapq.heapify(list)
        heapq.heappush(list, musica)

    print(list)
    return list


@app.route('/eletronica')
def eletronica():
    list = []
    #pegar dados com get
    requisicao = requests.get(
        f'{link}/.json'
    )  #colocando "&orderby" ao lado do .json, os dados retornam em ordem
    dic_requisicao = requisicao.json()
    print(dic_requisicao)
    for musica in dic_requisicao['musicas']['-NI07aBVl9jU1FK1QN_C'][
            'eletronica']:
        heapq.heapify(list)
        heapq.heappush(list, musica)

    print(list)
    return list


@app.route('/hino')
def pop():
    list = []
    #pegar dados com get
    requisicao = requests.get(
        f'{link}/.json'
    )  #colocando "&orderby" ao lado do .json, os dados retornam em ordem
    dic_requisicao = requisicao.json()
    print(dic_requisicao)
    for musica in dic_requisicao['musicas']['-NI07aBVl9jU1FK1QN_C']['hino']:
        heapq.heapify(list)
        heapq.heappush(list, musica)

    print(list)
    return list


#rodar a api com link no replit
app.run(host='0.0.0.0')
