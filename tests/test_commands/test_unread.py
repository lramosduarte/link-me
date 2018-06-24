from unittest import TestCase
from unittest.mock import Mock, patch

from linkme.file_managment import open_bookmarks_file, read_bookmarks
from linkme.commands.unread import (
    exibe_links_nao_lidos,
    open_link,
    procura_links_nao_lidos_por_email,
)


class UnreadCommandTestCase(TestCase):

    def setUp(self):
        self.dados_bookmarks = read_bookmarks(
            open_bookmarks_file('./tests/fakes/bookmarks.yml'))

    def test_procura_links_nao_lidos_por_email_return_all_unreads_urls(self):
        urls = procura_links_nao_lidos_por_email(self.dados_bookmarks)
        self.assertEqual(2, len(urls))

    @patch('linkme.commands.unread.open_link')
    def test_exibe_links_nao_lidos_in_terminal(self, mock_open_link):
        exibe_links_nao_lidos()
        mock_open_link.assert_called()

    @patch('webbrowser.open')
    @patch('builtins.input', Mock(return_value='0'))
    def test_open_link(self, mock_open):
        open_link([''])
        mock_open.assert_called()
