from collections import OrderedDict

import yaml


def open_bookmarks_file(bookmark_file='linkme/my_bookmark_template.yml'):
    return open(bookmark_file)


def read_bookmarks(arquivo=None):
    if not arquivo:
        arquivo = open_bookmarks_file()
    return yaml.load(arquivo)


def extrai_conjunto_bookmarks(dados):
    for k in dados.keys():
        yield dados[k]


def extrai_bookmark(lista_bookmarks):
    for b in lista_bookmarks:
        yield b


def extrai_urls(bookmarks, bookmark_read=False, all_bookmarks=False):
    urls_nao_lidas = OrderedDict()
    for bookmark in extrai_bookmark(bookmarks):
        if bookmark['read'] == bookmark_read or all_bookmarks:
            urls_nao_lidas[bookmark['url']] = None
    return urls_nao_lidas
