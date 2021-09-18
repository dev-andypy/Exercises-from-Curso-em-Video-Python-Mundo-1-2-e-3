import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http//www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessível no meomento')
else:
    print('Consegui acessar o site pudim com sucesso')
    print(site.read())