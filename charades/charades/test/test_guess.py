"""Tests for the guess.html and associated view"""
import httplib
import socket

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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
        self.browser.refresh()

    def test_generic_page_elements(self):
        """
        Test that the expected generic elements are on the guess.html page
        """
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Viewer'))
        self.browser.get('%s%s' % (self.live_server_url, '/guess'))
        self.assertEqual('Guess the phrase',
                         self.browser.find_element_by_class_name('page_title').text)
        self.assertIsNotNone(self.browser.find_element_by_id('guess_info'))
        self.assertEqual('Topic: Sport',
                         self.browser.find_element_by_id('topic').text,)
        self.assertEqual('Total words: 2',
                         self.browser.find_element_by_id('total_words').text)
        self.assertEqual('Current word: 1',
                         self.browser.find_element_by_id('current_word').text)
        self.assertEqual('You have 0 points',
                         self.browser.find_element_by_id('points_para').text)
        self.assertIsNotNone(self.browser.find_element_by_id('guess_input'))
        self.assertIsNotNone(self.browser.find_element_by_id('guess_form'))
        self.assertIsNotNone(self.browser.find_element_by_id('guess_field'))
        self.assertEqual('Guess Word',
                         self.browser.find_element_by_id('guess_word').get_attribute("value"))
        self.assertEqual('Guess Phrase',
                         self.browser.find_element_by_id('guess_phrase').get_attribute("value"))

    def test_single_word_phrase(self):
        """
        Test that the current word is not displayed when the phrase only has one word
        """
        self.browser.get('%s%s' % (self.live_server_url, '/acting/?phrase=Tennis'))
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Viewer'))
        self.browser.get('%s%s' % (self.live_server_url, '/guess'))
        try:
            self.browser.find_element_by_id('current_word')
            self.browser.find_element_by_id('guess_phrase')
        except NoSuchElementException:
            pass
        else:
            self.fail('No exception found when search for current word')
        guess_field = self.browser.find_element_by_id('guess_field')
        guess_field.send_keys("test")
        guess_word_button = self.browser.find_element_by_id('guess_phrase')
        guess_word_button.click()
        self.assertTrue('guess=test' in self.browser.current_url)
        self.assertTrue('guess_type=Guess+Phrase' in self.browser.current_url)

    def test_multi_word_phrase(self):
        """
        Test that the multi word interface is correct and adds
        the correct information to GET
        """
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Viewer'))
        self.browser.get('%s%s' % (self.live_server_url, '/guess'))
        guess_field = self.browser.find_element_by_id('guess_field')
        guess_field.send_keys("test")
        guess_word_button = self.browser.find_element_by_id('guess_phrase')
        guess_word_button.click()
        self.assertTrue('guess=test' in self.browser.current_url)
        self.assertTrue('guess_type=Guess+Phrase' in self.browser.current_url)

    def tearDown(self):
        self.browser.get('%s%s' % (self.live_server_url, '/reset'))
        self.browser.refresh()

    @classmethod
    def tearDownClass(cls):
        """
        Close webdriver instance
        """
        cls.browser.refresh()
        cls.browser.quit()
        super(TestGuess, cls).tearDownClass()
