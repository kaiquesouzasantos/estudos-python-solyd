# ===================== imports =====================

# import <nome_da_biblioteca>
# pip3/pip install => download para o python

# pip3 install requests => requisições web
import requests

# requests.get('<endereço_web>')
# requests.post('<endereço_web>')
# requests.delete('<endereço_web>')

request = requests.get('http://solyd.com.br')
print(request) # 200 => status maximo/estável # 404 => default
print(type(request))

# <nome_da_request_var> . <tipo_extração>
print(request.text)
print(request.status_code)
print(request.content)
print(request.headers)

try:
    request2 = requests.get('http://solyd.com.br')
    print(request2.status_code)
except Exception as E:
    print('deu pau',E)
