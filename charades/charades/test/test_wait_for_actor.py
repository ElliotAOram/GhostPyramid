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
        self.browser.get('%s%s' % (self.live_server_url, '/acting/?phrase=Tennis'))
        self.browser.get('%s%s' % (self.live_server_url, 
                                   '/instructions/?session_id=BSW18&user_type=Viewer'))
        self.browser.get('%s%s' % (self.live_server_url, '/guess'))
        # Submit correct guess
        self.browser.find_element_by_id('guess_field').send_keys("Tennis")
        self.browser.find_element_by_id('guess_word').click()
        self.browser.refresh()

    def test_generic_page_elements(self):
        """
        Test that the expected generic elements are on the guess.html page
        """
        self.assertTrue('wait_for_actor' in self.browser.current_url)
        self.assertEqual(self.browser.find_element_by_id('correct_guess').text, 
                         'You guessed the phrase \'Tennis\' correctly!')
        self.assertEqual(self.browser.find_element_by_id('points').text,
                         'You are first: 20points')
        self.assertEqual(self.browser.find_element_by_id('waiting').text,
                         'Waiting for the actor to select a new Phrase')


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
