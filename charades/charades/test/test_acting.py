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

    def setUp(self):
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Actor'))

    def test_page_basic_page_elements(self):
        """
        Test the basic contents of the index
        """
        self.browser.get('%s%s' % (self.live_server_url, '/acting/?phrase=Tennis'))
        self.assertTrue('Charades' in self.browser.title)
        page_title = self.browser.find_element_by_class_name('page_title')
        self.assertIsNotNone(page_title)

    def test_buttons_present_multi_word(self):
        """
        Tests that the buttons for word selection are present when the
        phrase contains multiple words
        """
        self.browser.get('%s%s' % (self.live_server_url, '/acting/?phrase=Shot+put'))
        button = self.browser.find_element_by_xpath( \
            "//form[@id='word_selection']/input["+ str(1) +"]")
        self.assertEqual(str(1), button.get_attribute("value"))
        button.click()
        self.assertTrue('current_word_index=' + str(1) in self.browser.current_url)
        button = self.browser.find_element_by_xpath( \
            "//form[@id='word_selection']/input["+ str(1) +"]")
        self.assertEqual(button.get_attribute("class"), "current_word_button")

    def test_complete_button(self):
        """
        Tests that the complete word button works
        """
        self.browser.get('%s%s' % (self.live_server_url, '/acting/?phrase=Shot+put'))
        self.browser.get('%s%s' % (self.live_server_url, '/acting/?current_word_index=1'))
        self.assertEqual(self.browser.find_element_by_class_name( \
                         'current_word_button').get_attribute('value'), '1')


        #TODO : Need to use a second web instance due to client side information conflict
        #       Or resolve conflict by different means?
        '''self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Viewer'))
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/guess/?guess=Shot&guess_type=Guess+Word'))
        self.browser.get('%s%s' % (self.live_server_url, '/acting/?word_complete=True'))
        self.assertEqual(self.browser.find_element_by_class_name( \
                          'completed_word_button').get_attribute('value'), '1')'''

    def tearDown(self):
        self.browser.refresh()
        self.browser.get('%s%s' % (self.live_server_url, '/reset'))
        self.browser.refresh()

    @classmethod
    def tearDownClass(cls):
        """
        Close webdriver instance
        """
        cls.browser.refresh()
        cls.browser.quit()
        super(ActingTests, cls).tearDownClass()
