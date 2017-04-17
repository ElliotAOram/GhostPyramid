"""Tests for the phrase_ready api"""
import re
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class PhraseReadyAPITests(StaticLiveServerTestCase):
    """
    Phrase_ready api test
    """

    @classmethod
    def setUpClass(cls):
        """
        Start chrome instance of webdriver
        """
        super(PhraseReadyAPITests, cls).setUpClass()
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(10)

    def test_false_api_state(self):
        self.browser.get('%s%s' % (self.live_server_url, '/api/phrase_ready/'))
        text_found = re.search(r'False', self.browser.page_source)
        self.assertNotEqual(text_found, None)

    def test_true_api_state(self):
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Actor'))
        self.browser.get('%s%s' % (self.live_server_url, '/acting/?phrase=Tennis'))
        self.browser.get('%s%s' % (self.live_server_url, '/api/phrase_ready/'))
        text_found = re.search(r'True', self.browser.page_source)
        self.assertNotEqual(text_found, None)

    def tearDown(self):
        self.browser.get('%s%s' % (self.live_server_url, '/reset'))

    @classmethod
    def tearDownClass(cls):
        """
        Close webdriver instance
        """
        cls.browser.refresh()
        cls.browser.quit()
        super(PhraseReadyAPITests, cls).tearDownClass()
