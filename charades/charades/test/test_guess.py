"""Tests for the guess.html and associated view"""
import httplib
import socket

from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class TestGuess(StaticLiveServerTestCase):
    """
    guess.html for page elements and button transistions
    """

    @classmethod
    def setUpClass(cls):
        """
        Start chrome instance of webdriver
        """
        super(TestGuess, cls).setUpClass()
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(10)

    def setUp(self):
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Actor'))
        self.browser.get('%s%s' % (self.live_server_url, '/acting/?phrase=Shot+Put'))
        self.browser.get('%s%s' % (self.live_server_url, '/acting/?current_word_index=1'))
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Viewer'))
        self.browser.refresh()

    def test_generic_page_elements(self):
        """
        Test that the expected generic elements are on the guess.html page
        """
        self.browser.get('%s%s' % (self.live_server_url, '/1/guess'))
        self.assertEqual('Guess the phrase',
                         self.browser.find_element_by_class_name('page_title').text)
        self.assertIsNotNone(self.browser.find_element_by_id('guess_info'))
        self.assertEqual('Topic: Sport',
                         self.browser.find_element_by_id('topic').text,)
        self.assertEqual('Total words: 2',
                         self.browser.find_element_by_id('total_words').text)
        self.assertEqual('Current word: 1',
                         self.browser.find_element_by_id('current_word').text)
        self.assertIsNotNone(self.browser.find_element_by_id('guess_input'))
        self.assertIsNotNone(self.browser.find_element_by_id('guess_form'))
        self.assertIsNotNone(self.browser.find_element_by_id('guess_field'))
        self.assertEqual('Guess Word',
                         self.browser.find_element_by_id('guess_word').get_attribute("value"))
        self.assertEqual('Guess Phrase',
                         self.browser.find_element_by_id('guess_phrase').get_attribute("value"))

    def test_multi_user(self):
        """
        Test that when two users sign in, they have different urls in guess.html
        """
        self.browser.find_element_by_id('continue_button').click()
        self.browser.refresh()
        first_url = self.browser.current_url
        self.browser.quit()
        browser2 = webdriver.Chrome()
        browser2.implicitly_wait(10)
        browser2.get('%s%s' % (self.live_server_url,
                               '/instructions/?session_id=BSW18&user_type=Viewer'))
        browser2.find_element_by_id('continue_button').click()
        second_url = browser2.current_url
        browser2.quit()
        self.assertNotEqual(first_url, second_url)
        self.assertTrue('guess' in first_url)
        self.assertTrue('guess' in second_url)

    # http://stackoverflow.com/questions/28934533/python-selenium-how-to-check-whether-the-webdriver-did-quit
    def tearDown(self):
        try:
            self.browser.refresh()
        except (socket.error, httplib.CannotSendRequest):
            return True

    @classmethod
    def tearDownClass(cls):
        """
        Close webdriver instance
        """
        try:
            cls.browser.refresh()
            cls.browser.quit()
        except (socket.error, httplib.CannotSendRequest):
            pass
        super(TestGuess, cls).tearDownClass()
