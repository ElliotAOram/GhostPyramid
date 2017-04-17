"""Tests for the phrase_ready api"""
import re
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class GuessCorrectAPITests(StaticLiveServerTestCase):
    """
    Phrase_ready api test
    """

    @classmethod
    def setUpClass(cls):
        """
        Start chrome instance of webdriver
        """
        super(GuessCorrectAPITests, cls).setUpClass()
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(10)

    def test_none_api_state(self):
        self.browser.get('%s%s' % (self.live_server_url, '/api/guess_correct/'))
        text_found = re.search(r'None', self.browser.page_source)
        self.assertNotEqual(text_found, None)

    def test_word_api_state(self):
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Actor'))
        self.browser.get('%s%s' % (self.live_server_url, '/acting/?phrase=Shot+Put'))
        self.browser.get('%s%s' % (self.live_server_url, '/acting/?current_word=Put'))
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Viewer/'))
        self.browser.get('%s%s' % (self.live_server_url, '/guess/'))
        self.browser.get('%s%s' % (self.live_server_url, '/guess/Guess+Word=Put'))
        self.browser.get('%s%s' % (self.live_server_url, '/api/guess_correct'))
        text_found = re.search(r'Word', self.browser.page_source)
        self.assertNotEqual(text_found, None)

    def test_phrase_api_state(self):
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Actor'))
        self.browser.get('%s%s' % (self.live_server_url, '/acting/?phrase=Tennis'))
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Viewer/'))
        self.browser.get('%s%s' % (self.live_server_url, '/guess/'))
        self.browser.get('%s%s' % (self.live_server_url, '/guess/Guess+Phrase=Tennis'))
        self.browser.get('%s%s' % (self.live_server_url, '/api/guess_correct'))
        text_found = re.search(r'Phrase', self.browser.page_source)
        self.assertNotEqual(text_found, None)

    @classmethod
    def tearDownClass(cls):
        """
        Close webdriver instance
        """
        cls.browser.refresh()
        cls.browser.quit()
        super(GuessCorrectAPITests, cls).tearDownClass()
