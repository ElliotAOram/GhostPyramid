"""Tests for the instructions.html and associated view"""
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from charades import strings

class InstructionsTests(StaticLiveServerTestCase):
    """
    Index.html tests for page elements and button uses
    """

    @classmethod
    def setUpClass(cls):
        """
        Start chrome instance of webdriver
        """
        super(InstructionsTests, cls).setUpClass()
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(10)


    def test_generic_page_elements(self):
        """
        Test the non-actor and non-viewer spesific content
        """
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18'))
        self.assertTrue('Charades' in self.browser.title)
        self.assertEqual('Instructions',
                         self.browser.find_element_by_class_name('page_title').text)
        self.assertIsNotNone(self.browser.find_element_by_id('instructions_cont'))
        self.assertEqual('Continue',
                         self.browser.find_element_by_id('continue_button').get_attribute("value"))

    def test_page_elements_actor(self):
        """
        Test the elements of the actor page
        """
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Actor'))
        self.assertEqual(strings.actor_instructions(),
                         self.browser.find_element_by_id('instruction_para').text)

    def test_actor_button_click(self):
        """
        Test that the actor button for phrase selection
        moves the user to the phrase_selection.html page
        """
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Actor'))
        continue_button = self.browser.find_element_by_id('continue_button')
        continue_button.click()
        self.assertTrue(self.live_server_url + '/select_phrase/' in self.browser.current_url)

    def test_page_elements_viewer(self):
        """
        Test the elements of the viewer page
        """
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Viewer'))
        self.assertEqual(strings.viewer_instructions(),
                         self.browser.find_element_by_id('instruction_para').text)

    def test_viewer_button_click(self):
        """
        Test the viewer instance of the continue button leads to the guess page
        """
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Actor'))
        self.browser.get('%s%s' % (self.live_server_url, '/acting/?phrase=Shot+put'))
        self.browser.get('%s%s' % (self.live_server_url,
                                   '/instructions/?session_id=BSW18&user_type=Viewer'))
        continue_button = self.browser.find_element_by_id('continue_button')
        continue_button.click()
        self.assertTrue('/guess' in self.browser.current_url)
        # Need additional test for viewer_number in url

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
        super(InstructionsTests, cls).tearDownClass()
