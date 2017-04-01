"""Tests for the guess.html and associated view"""
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
        self.browser.get('%s%s' % (self.live_server_url, '/instructions/?session_id=BSW18&user_type=Viewer'))
        self.browser.refresh()

    def test_generic_page_elements(self):
        """
        Test that the expected generic elements are on the guess.html page
        """
        self.browser.get('%s%s' % (self.live_server_url, '/1/guess'))
        self.assertEqual('Guess the phrase', self.browser.find_element_by_class_name('page_title').text)
        self.assertIsNotNone(self.browser.find_element_by_id('guess_info'))
        self.assertIsNotNone(self.browser.find_element_by_id('guess_input'))
        self.assertIsNotNone(self.browser.find_element_by_id('guess_form'))
        self.assertIsNotNone(self.browser.find_element_by_id('guess_field'))
        self.assertEqual('Guess Word', 
                         self.browser.find_element_by_id('guess_word').get_attribute("value"))
        self.assertEqual('Guess Phrase',
                         self.browser.find_element_by_id('guess_phrase').get_attribute("value"))
        

    def tearDown(self):
        self.browser.refresh()

    @classmethod
    def tearDownClass(cls):
        """
        Close webdriver instance
        """
        cls.browser.refresh()
        cls.browser.quit()
        super(TestGuess, cls).tearDownClass()
