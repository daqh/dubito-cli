import unittest
from unittest import mock
from dubito import subito_detail_page, subito_list_page

test_subito_list_page = open("tests/data/test_subito_list_page.html", "r").read()

class TestSubitoListPage(unittest.TestCase):

    def test_subito_list_page_without_page_number(self):
        url = "https://www.subito.it/annunci-italia/vendita/usato/?q=gtx%201070"
        page = subito_list_page.SubitoListPage(url)
        self.assertEqual(page.page_number, 1, "The page number should be 1 if not specified.")

    def test_subito_list_page_with_page_number(self):
        url = "https://www.subito.it/annunci-italia/vendita/usato/?q=gtx%201070&o=2"
        page = subito_list_page.SubitoListPage(url)
        self.assertEqual(page.page_number, 2, "The page number should be 2 if specified.")

    def test_subito_list_page_without_query(self):
        url = "https://www.subito.it/annunci-italia/vendita/usato/?o=2"
        with self.assertRaises(ValueError):
            page = subito_list_page.SubitoListPage(url)

    def test_subito_list_page(self):
        url = "https://www.subito.it/annunci-italia/vendita/usato/?q=gtx%201070&o=2"
        page = subito_list_page.SubitoListPage(url)
        self.assertEqual(page.url, url, "The url should be the same as the one passed to the constructor.")
        self.assertEqual(page.query, "gtx 1070", "The query should be the same as the one passed to the constructor.")

    def test_subito_list_page_getitem(self):
        page = subito_list_page.SubitoListPage("https://www.subito.it/annunci-italia/vendita/usato/?q=gtx%201070&o=1")
        self.assertEqual(page[3].url, "https://www.subito.it/annunci-italia/vendita/usato/?q=gtx%201070&o=3", "The url should be the same as the one passed to the constructor but with the new page.")
        self.assertEqual(page[2].query, "gtx 1070", "The query should be the same as the one passed to the constructor.")
        self.assertEqual(page[5].page_number, 5, "The page number should be 2 if specified.")

    def test_subito_query_list_page(self):
        page = subito_list_page.SubitoQueryListPage("gtx 1070")
        self.assertEqual(page.url, "https://www.subito.it/annunci-italia/vendita/usato/?q=gtx%201070&o=1", "The url should be the same as the one passed to the constructor.")
        self.assertEqual(page.query, "gtx 1070", "The query should be the same as the one passed to the constructor.")
        self.assertEqual(page.page_number, 1, "The page number should be 1 if not specified.")

class TestExtractedSubitoListPage(unittest.TestCase):

    @mock.patch("requests.get", return_value=mock.Mock(status_code=200, text=test_subito_list_page))
    def test_extracted_subito_list_page(self, _):
        url = "https://www.subito.it/annunci-italia/vendita/usato/?q=gtx%201070&o=2"
        page = subito_list_page.SubitoListPage(url)
        extracted_page = subito_list_page.ExtractedSubitoListPage(page)
        self.assertEqual(extracted_page.response, test_subito_list_page, "The text should be the same as the one passed to the constructor.")

    @mock.patch("requests.get", return_value=mock.Mock(status_code=200, text=test_subito_list_page))
    def test_extracted_subito_list_from_url(self, _):
        url = "https://www.subito.it/annunci-italia/vendita/usato/?q=gtx%201070&o=2"
        extracted_page = subito_list_page.ExtractedSubitoListPage.from_url(url)
        self.assertEqual(extracted_page.response, test_subito_list_page, "The text should be the same as the one passed to the constructor.")

    @mock.patch("requests.get", return_value=mock.Mock(status_code=200, text=test_subito_list_page))
    def test_extracted_subito_list_from_query(self, _):
        query = "gtx 1070"
        extracted_page = subito_list_page.ExtractedSubitoListPage.from_query(query)
        self.assertEqual(extracted_page.response, test_subito_list_page, "The text should be the same as the one passed to the constructor.")

class TestTransformedSubitoListPage(unittest.TestCase):

    @mock.patch("requests.get", return_value=mock.Mock(status_code=200, text=test_subito_list_page))
    def test_transformed_subito_list_page(self, _):
        url = "https://www.subito.it/annunci-italia/vendita/usato/?q=gtx%201070&o=2"
        page = subito_list_page.SubitoListPage(url)
        extracted_page = subito_list_page.ExtractedSubitoListPage(page)
        transformed_page = subito_list_page.TransformedSubitoListPage(extracted_page)
        self.assertEqual(len(transformed_page.subito_list_page_items), 33, "The number of insertions should be 33.")
        # Check that the keys are the same
        keys = transformed_page.subito_list_page_items[0].keys()
        self.assertTrue("title" in keys, "The insertion should have a title.")
        self.assertTrue("price" in keys, "The insertion should have a price.")
        self.assertTrue("thumbnail" in keys, "The insertion should have a price.")
        self.assertTrue("url" in keys, "The insertion should have a location.")
        self.assertTrue("city" in keys, "The insertion should have a date.")
        self.assertTrue("sold" in keys, "The insertion should have a url.")
        self.assertTrue("state" in keys, "The insertion should have a url.")
        self.assertTrue("time" in keys, "The insertion should have a url.")
        self.assertTrue("page" in keys, "The insertion should have a url.")
        self.assertTrue("timestamp" in keys, "The insertion should have a url.")

test_subito_detail_page = open("tests/data/test_subito_detail_page.html", "r").read()

class TestSubitoDetailPage(unittest.TestCase):

    def test_subito_detail_page(self):
        url = "https://www.subito.it/informatica/pc-desktop-gaming-i7-8700k-rtx-2080-16gb-ram-ssd-500gb-roma-337616447.htm"
        page = subito_detail_page.SubitoDetailPage(url)
        self.assertEqual(page.url, url, "The url should be the same as the one passed to the constructor.")

class TestExtractedSubitoDetailPage(unittest.TestCase):

    @mock.patch("requests.get", return_value=mock.Mock(status_code=200, text=test_subito_detail_page))
    def test_extracted_subito_detail_page(self, _):
        url = "https://www.subito.it/informatica/pc-desktop-gaming-i7-8700k-rtx-2080-16gb-ram-ssd-500gb-roma-337616447.htm"
        page = subito_detail_page.SubitoDetailPage(url)
        extracted_page = subito_detail_page.ExtractedSubitoDetailPage(page)
        self.assertEqual(extracted_page.response, test_subito_detail_page, "The text should be the same as the one passed to the constructor.")

class TestTransformedSubitoDetailPage(unittest.TestCase):

    @mock.patch("requests.get", return_value=mock.Mock(status_code=200, text=test_subito_detail_page))
    def test_transformed_subito_detail_page(self, _):
        url = "https://www.subito.it/informatica/pc-desktop-gaming-i7-8700k-rtx-2080-16gb-ram-ssd-500gb-roma-337616447.htm"
        page = subito_detail_page.SubitoDetailPage(url)
        extracted_page = subito_detail_page.ExtractedSubitoDetailPage(page)
        transformed_page = subito_detail_page.TransformedSubitoDetailPage(extracted_page)
        self.assertEqual(transformed_page.subito_detail_page_item["title"], "PC Gaming Ryzen 7 1700/GTX 1070 ti")
        self.assertEqual(transformed_page.subito_detail_page_item["price"], 650)
        self.assertEqual(transformed_page.subito_detail_page_item["sold"], False)
        self.assertEqual(transformed_page.subito_detail_page_item["city"], "Ravenna")
        self.assertEqual(transformed_page.subito_detail_page_item["state"], "(RA)")
