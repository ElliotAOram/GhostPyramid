"""Tests for the index.html and associated view"""
from selenium import webdriver
from django.test import LiveServerTestCase

#https://pypi.python.org/pypi/selenium
#https://docs.djangoproject.com/en/1.8/topics/testing/tools/#liveservertestcase

class IndexTests(LiveServerTestCase):
    """
    Index.html tests for page elements and button uses
    """

    def setUp(self):
        """
        Start chrome instance of webdriver
        """
        self.browser = webdriver.Chrome()
        self.browser.get('http://localhost:8081')

    def tearDown(self):
        """
        Close webdriver instance
        """
        self.browser.quit()

    def test_page_elements(self):
        """
        Test the basic contents of the index
        """
        self.assertTrue('Charades' in self.browser.title)
        page_title = self.browser.find_element_by_class_name('page_title')
        self.assertIsNotNone(page_title)
        login_form = self.browser.find_element_by_id('login_form')
        self.assertIsNotNone(login_form)
        session_id = self.browser.find_element_by_name('session_id')
        self.assertIsNotNone(session_id)
        actor_button = self.browser.find_element_by_id('actor_button')
        self.assertIsNotNone(actor_button)
        viewer_button = self.browser.find_element_by_id('viewer_button')
        self.assertIsNotNone(viewer_button)

    def test_actor_button(self):
        """
        Test that the actor button navigates to the instruction page
        """
        actor_button = self.browser.find_element_by_id('actor_button')
        actor_button.click()
        current_url = self.browser.current_url
        self.assertTrue(r'localhost:8081/instructions/' in current_url)
        self.assertTrue('user_type=Actor' in current_url)

    def test_viewer_button(self):
        """
        Test that the viewer button navigates to the instruction page
        """
        viewer_button = self.browser.find_element_by_id('viewer_button')
        viewer_button.click()
        current_url = self.browser.current_url
        self.assertTrue(r'localhost:8081/instructions/' in current_url)
        self.assertTrue('user_type=Viewer' in current_url)
