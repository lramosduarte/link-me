from unittest import TestCase

from linkme.file_managment import (
    extrai_bookmark,
    extrai_conjunto_bookmarks,
    extrai_urls,
    open_bookmarks_file,
    read_bookmarks,
)


class FileManagmentTestCase(TestCase):

    def test_open_file_with_sucess(self):
        open_bookmarks_file('./tests/fakes/bookmarks.yml')

    def test_read_bookmarks_with_sucess(self):
        dados_bookmarks = read_bookmarks(
            open_bookmarks_file('./tests/fakes/bookmarks.yml'))
        self.assertIsNotNone(dados_bookmarks)


class FileManagmentWithDataLoadTestCase(TestCase):

    def setUp(self):
        self.dados_bookmarks = read_bookmarks(
            open_bookmarks_file('./tests/fakes/bookmarks.yml'))

    def test_extrai_conjunto_bookmarks_by_key(self):
        dataset = next(extrai_conjunto_bookmarks(self.dados_bookmarks))
        self.assertTrue(dataset.keys())

    def test_extrai_bookmark_with_success(self):
        dataset = next(extrai_conjunto_bookmarks(self.dados_bookmarks))
        data = next(extrai_bookmark(dataset['urls']))
        self.assertIn('read', data)

    def test_extrai_urls_return_list_by_default_unread_urls(self):
        dataset = next(extrai_conjunto_bookmarks(self.dados_bookmarks))
        urls = extrai_urls(dataset['urls'])
        self.assertEqual(1, len(urls))

    def test_extrai_urls_return_list_read_urls(self):
        dataset = self.dados_bookmarks['shared']
        urls = extrai_urls(dataset['other.user+1@gmail.com']['urls'], bookmark_read=True)
        self.assertEqual(2, len(urls))

    def test_extrai_urls_return_list_all_urls(self):
        dataset = next(extrai_conjunto_bookmarks(self.dados_bookmarks))
        urls = extrai_urls(dataset['urls'], all_bookmarks=True)
        self.assertEqual(2, len(urls))
