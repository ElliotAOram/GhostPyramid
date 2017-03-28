"""Tests for the acting.html and associated view"""
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class ActingTests(StaticLiveServerTestCase):
    """
    Acting.html tests for page elements and button uses
    """

    @classmethod
    def setUpClass(cls):
        """
        Start chrome instance of webdriver
        """
        super(ActingTests, cls).setUpClass()
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(10)

    def test_page_basic_page_elements(self):
        """
        Test the basic contents of the index
        """
        self.browser.get('%s%s' % (self.live_server_url, '/acting/'))
        self.assertTrue('Charades' in self.browser.title)
        page_title = self.browser.find_element_by_class_name('page_title')
        self.assertIsNotNone(page_title)

    def tearDown(self):
        self.browser.refresh()

    @classmethod
    def tearDownClass(cls):
        """
        Close webdriver instance
        """
        cls.browser.refresh()
        cls.browser.quit()
        super(ActingTests, cls).tearDownClass()
