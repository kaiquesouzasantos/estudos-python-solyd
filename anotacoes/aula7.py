# ===================== argumentos =====================
#pip install 

import sys
argumentos = sys.argv

def soma(n1,n2):
    return n1 + n2

def sub():
    return n1 - n2

if argumentos[1] == "soma":
    resp = soma(argumentos[2]), argumentos[3]
elif argumentos[1] == "sub":
    resp = sub(argumentos[2],argumentos[3])
print(resp)

