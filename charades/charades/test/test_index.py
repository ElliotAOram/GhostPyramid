"""Tests for the index.html and associated view"""
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


#https://pypi.python.org/pypi/selenium
#https://docs.djangoproject.com/en/1.8/topics/testing/tools/#liveservertestcase

class IndexTests(StaticLiveServerTestCase):
    """
    Index.html tests for page elements and button uses
    """

    @classmethod
    def setUpClass(cls):
        """
        Start chrome instance of webdriver
        """
        super(IndexTests, cls).setUpClass()
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(10)


    def test_page_elements(self):
        """
        Test the basic contents of the index
        """
        self.browser.get('%s' % (self.live_server_url))
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
        self.browser.get('%s' % (self.live_server_url))
        actor_button = self.browser.find_element_by_id('actor_button')
        actor_button.click()
        current_url = self.browser.current_url
        self.assertTrue(r'localhost:8081/instructions/' in current_url)
        self.assertTrue('user_type=Actor' in current_url)


    def test_viewer_button(self):
        """
        Test that the viewer button navigates to the instruction page
        """
        self.browser.get('%s' % (self.live_server_url))
        viewer_button = self.browser.find_element_by_id('viewer_button')
        viewer_button.click()
        current_url = self.browser.current_url
        self.assertTrue(r'localhost:8081/instructions/' in current_url)
        self.assertTrue('user_type=Viewer' in current_url)

    # http://stackoverflow.com/questions/13243267/django-and-selenium-web-testing-error-errno-10054
    def tearDown(self):
        self.browser.refresh()

    @classmethod
    def tearDownClass(cls):
        """
        Close webdriver instance
        """
        cls.browser.refresh()
        cls.browser.quit()
        super(IndexTests, cls).tearDownClass()
