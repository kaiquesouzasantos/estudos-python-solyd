# ===================== API =====================

# http://www.omdbapi.com => API de Filmes

import requests
import json # lib para manipulação de arquivos JSON, já vem embutida no python version

try:
    request = requests.get('http://www.omdbapi.com/?t=1917')
except Exception:
    print('deu pau na conexão')
    exit() # exit => sair so programa, semelhante ao BREAK
print(request.text)

dic = json.loads(request.text) # loads => JSON para dict
print(dic)






























