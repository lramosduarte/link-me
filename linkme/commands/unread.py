from collections import OrderedDict

import webbrowser


from linkme.file_managment import (
    read_bookmarks,
    extrai_conjunto_bookmarks,
    extrai_urls,
)


def procura_links_nao_lidos_por_email(dados_por_email):
    urls_nao_lidas = OrderedDict()
    for dados in extrai_conjunto_bookmarks(dados_por_email):
        if 'urls' in dados:
            urls_nao_lidas.update(extrai_urls(dados['urls'], bookmark_read=False))
        elif isinstance(dados, dict):
            urls_nao_lidas.update(procura_links_nao_lidos_por_email(dados))
    return urls_nao_lidas


def exibe_links_nao_lidos():
    urls_nao_lidas = procura_links_nao_lidos_por_email(read_bookmarks())
    print('Unread bookmarks:')
    for indice, url in enumerate(urls_nao_lidas):
        print('{choice}: '.format(choice=indice), url)
    print('What link do you wish open?(The link will open in native browser)')
    open_link(list(urls_nao_lidas.keys()))


def open_link(lista_urls):
    choice = int(input())
    webbrowser.open(lista_urls[choice])
