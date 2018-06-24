import json
import requests

from linkme.file_managment import open_bookmarks_file


FILE_IO = 'https://file.io/?expires={time}'


def fileio_uploader(arquivo, time='1d'):
    resposta = requests.post(
        FILE_IO.format(time=time),
        files={'file': arquivo},
    )
    dados_resposta = json.loads(resposta.content)
    if resposta.status_code == 200 and dados_resposta['success']:
        return dados_resposta['link']


def upload_file():
    print(fileio_uploader(open_bookmarks_file()))
