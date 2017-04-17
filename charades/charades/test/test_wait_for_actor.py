"""Tests for the guess.html and associated view"""

from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class TestWaitForActor(StaticLiveServerTestCase):
    """
    guess.html for page elements and button transistions
    """

    @classmethod
    def setUpClass(cls):
        """
        Start chrome instance of webdriver
        """
        super(TestWaitForActor, cls).setUpClass()
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(10)

    def setUp(self):
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Actor'))
        self.browser.get('%s%s' % (self.live_server_url, '/acting/?phrase=Shot+Put'))
        self.browser.get('%s%s' % (self.live_server_url, '/acting/?current_word_index=1'))
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Viewer'))
        self.browser.get('%s%s' % (self.live_server_url, '/guess'))


    def test_phrase_page_elements(self):
        """
        Test that the expected generic elements are on the guess.html page
        """
        self.browser.find_element_by_id('guess_field').send_keys("Shot Put")
        self.browser.find_element_by_id('guess_phrase').click()
        self.browser.refresh()
        self.assertTrue('waiting_for_actor' in self.browser.current_url)
        self.assertEqual(self.browser.find_element_by_id('correct_guess').text,
                         'You guessed the Phrase Shot Put correctly!')
        self.assertEqual(self.browser.find_element_by_id('points_position').text,
                         'You are 1st:\n20 points')
        self.assertEqual(self.browser.find_element_by_id('waiting').text,
                         'Waiting for the actor to select a new Phrase')

    def test_phrase_page_elements(self):
        """
        Test that the expected generic elements are on the guess.html page
        """
        self.browser.find_element_by_id('guess_field').send_keys("Shot")
        self.browser.find_element_by_id('guess_word').click()
        self.browser.refresh()
        self.assertTrue('waiting_for_actor' in self.browser.current_url)
        self.assertEqual(self.browser.find_element_by_id('correct_guess').text,
                         'You guessed the Word Shot correctly!')
        self.assertEqual(self.browser.find_element_by_id('points_position').text,
                         'You are 1st:\n10 points')
        self.assertEqual(self.browser.find_element_by_id('waiting').text,
                         'Waiting for the actor to select a new Word')


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
        super(TestWaitForActor, cls).tearDownClass()
