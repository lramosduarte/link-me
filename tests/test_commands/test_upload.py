from unittest import TestCase
from unittest.mock import Mock, patch

import json

from linkme.commands.upload import fileio_uploader, upload_file
from linkme.file_managment import open_bookmarks_file
from tests.fakes import fileio_response


def mock_resposta_fileIO():
    mock = Mock()
    mock.content = fileio_response.content
    mock.status_code = 200
    return mock


class UploadCommandTestCase(TestCase):

    def setUp(self):
        self.arquivo = open_bookmarks_file('./tests/fakes/bookmarks.yml')

    @patch('requests.post', Mock(return_value=mock_resposta_fileIO()))
    def test_fileio_uploader_send_file_with_success(self):
        url = fileio_uploader(self.arquivo)
        expected = json.loads(fileio_response.content)['link']
        self.assertEqual(expected, url)

    @patch('linkme.commands.upload.fileio_uploader', Mock(return_value='http://'))
    def test_upload_file_show_url_with_success(self):
        upload_file()
