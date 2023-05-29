import unittest
from unittest import mock
from dubito import subito_detail_page, subito_list_page

test_subito_list_page = open("tests/data/test_subito_list_page.html", "r").read()

class TestSubitoListPage(unittest.TestCase):

    def test_subito_list_page_without_page_number(self):
        url = "https://www.subito.it/annunci-italia/vendita/usato/?q=gtx%201070"
        list_page = subito_list_page.SubitoListPage(url)
        self.assertEqual(list_page.url, url, "The url is not the same")
        self.assertEqual(list_page.page_number, 1, "The page number is not the same")
        self.assertEqual(list_page.query, "gtx 1070", "The query is not the same")
        self.assertEqual(list_page[2].page_number, 2, "The page number is not the same")

    def test_subito_list_page_with_page_number(self):
        url = "https://www.subito.it/annunci-italia/vendita/usato/?q=gtx%201070&o=2"
        list_page = subito_list_page.SubitoListPage(url)
        self.assertEqual(list_page.url, url, "The url is not the same")
        self.assertEqual(list_page.page_number, 2, "The page number is not the same")

    def test_subito_list_page_without_query(self):
        url = "https://www.subito.it/annunci-italia/vendita/usato/"
        self.assertRaises(ValueError, subito_list_page.SubitoListPage, url)

class TestSubitoListPageQuery(unittest.TestCase):

    def test_subito_list_page_query_without_page_number(self):
        list_page = subito_list_page.SubitoListPageQuery("gtx 1070")
        self.assertEqual(list_page.query, "gtx 1070", "The query is not the same")
        self.assertEqual(list_page.page_number, 1, "The page number is not the same")

    def test_subito_list_page_query_with_page_number(self):
        list_page = subito_list_page.SubitoListPageQuery("gtx 1070", 2)
        self.assertEqual(list_page.query, "gtx 1070", "The query is not the same")
        self.assertEqual(list_page.page_number, 2, "The page number is not the same")

    def test_subito_list_page_query_with_category(self):
        list_page = subito_list_page.SubitoListPageQuery("gtx 1070", category="informatica")
        self.assertEqual(list_page.query, "gtx 1070", "The query is not the same")
        self.assertEqual(list_page.page_number, 1, "The page number is not the same")
        self.assertEqual(list_page.url, "https://www.subito.it/annunci-italia/vendita/informatica/?q=gtx%201070&o=1", "The url is not the same")

    def test_subito_list_page_query_with_page_number(self):
        list_page = subito_list_page.SubitoListPageQuery("gtx 1070", category="informatica", page_number=2)
        self.assertEqual(list_page.query, "gtx 1070", "The query is not the same")
        self.assertEqual(list_page.page_number, 2, "The page number is not the same")
        self.assertEqual(list_page.url, "https://www.subito.it/annunci-italia/vendita/informatica/?q=gtx%201070&o=2", "The url is not the same")

class TestExtractedSubitoListPage(unittest.TestCase):

    def test_extracted_subito_list_page_without_page_number(self):
        list_page = subito_list_page.SubitoListPageQuery("gtx 1070")
        list_page = subito_list_page.extract(list_page)
        self.assertEqual(list_page.url, "https://www.subito.it/annunci-italia/vendita/usato/?q=gtx%201070&o=1", "The url is not the same")
        self.assertEqual(list_page.page_number, 1, "The page number is not the same")
        self.assertEqual(list_page.query, "gtx 1070", "The query is not the same")

    def test_extracted_subito_list_page_with_page_number(self):
        list_page = subito_list_page.SubitoListPageQuery("gtx 1070", 2)
        list_page = subito_list_page.extract(list_page)
        self.assertEqual(list_page.url, "https://www.subito.it/annunci-italia/vendita/usato/?q=gtx%201070&o=2", "The url is not the same")
        self.assertEqual(list_page.page_number, 2, "The page number is not the same")
        self.assertEqual(list_page.query, "gtx 1070", "The query is not the same")
