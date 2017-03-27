"""Tests for the select_phrase.html and associated view"""
from selenium import webdriver
from django.test import LiveServerTestCase

class SelectPhraseTests(LiveServerTestCase):
    """
    Select_Phrase.html for page elements and button transistions
    """

    @classmethod
    def setUpClass(cls):
        """
        Start chrome instance of webdriver
        """
        super(SelectPhraseTests, cls).setUpClass()
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(10)

    def test_generic_page_elements(self):
        self.browser.get('%s%s' % (self.live_server_url, '/select_phrase/'))
        self.assertTrue('Charades' in self.browser.title)
        page_title = self.browser.find_element_by_class_name('page_title').text
        self.assertEqual('Select Phrase', page_title)
        form = self.browser.find_element_by_id('phrase_selection_form')
        self.assertIsNotNone(form)

    def test_phrases_are_not_same(self):
        self.browser.get('%s%s' % (self.live_server_url, '/select_phrase/'))
        phrases = []
        for i in range(1, 6):
            phrases.append(self.browser.find_element_by_xpath( \
                "//form[@id='phrase_selection_form']/input["+str(i)+"]").get_attribute("value"))
        for idx, current_phrase in enumerate(phrases):
            sub_phrases = phrases
            sub_phrases.pop(idx)
            for next_phrase in phrases:
                self.assertNotEqual(current_phrase, next_phrase)
        self.browser.refresh()

    #def test_phrase_buttons_to_acting_page
    #    for index in range(1, 5):
    #        self.browser.get('%s%s', (self.live_server_url, '/select_phrase/'))
    #        phrase_button = self.browser.find_element_by_id('phrase' + str(index))
    #        phrase_button.click()
    #        self.assertTrue('/acting/' in self.live_server_url)
    #        self.browser.refresh()

    def tearDown(self):
        self.browser.refresh()

    @classmethod
    def tearDownClass(cls):
        """
        Close webdriver instance
        """
        cls.browser.refresh()
        cls.browser.quit()
        super(SelectPhraseTests, cls).tearDownClass()
