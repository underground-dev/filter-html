#import das bibliotecas necessarias 
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import *

#Welcome/menu
print("Bem vindo ao web-filter")
print("abaixo as requisições serão explicadas")

#variavel capture
url = input("url destino: ")
fil = input("queres filtros (Y/N): ")
if (fil == "Y"):
    fil_choise = input("tipo de filtros (class/id/tag/name): ")
    if (fil_choise != "tag"):
        fil_tagname = input("digite o nome da tag a ser pesquisada com os atributos")
        fil_atrribname = input("nome do atributo a ser pesquisado")
        fil_attrib = input("digite o conteudo do atributo a ser encontrado")
    else:
        fil_define = input("declare nome da tag a ser filtrado: ")

    #usando variaveis dentro do bloco try
        try:
            #obtendo a pagina
            html = urlopen(url)
            obj = BeautifulSoup(html.read(), "html5lib")
        except HTTPError as e:
            #tratando erros
            print(e)
        except URLError:
            print("servidores não respondem ou url incorreta")
        else:
            #iniciando filtro
            if (fil_choise == "tag"):
                tags = obj.fil_define
                if (tags is None):
                    print("tag não encontrada")
                else:
                    for tag in tags:
                        print(tag)
            else:
                tags = obj.findall(fil_tagname, {fil_atrribname:fil_attrib})
                for tag in tags:
                    print(tag.getText())
else:
    #buscando pagina sem filtro
    try:
        html = urlopen(url)
        obj = BeautifulSoup(html.read(),"html5lib")
    except HTTPError as e:
        print(e)
    except URLError:
        print("servers indisponiveis ou url incorreta")
    else:
        print(obj.getText())

