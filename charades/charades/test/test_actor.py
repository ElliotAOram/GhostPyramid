"""Testing module for actor class"""
import unittest
from charades.actor import Actor

class TestActor(unittest.TestCase):
    """
    Tests for the actor.py Actor class
    """

    def setUp(self):
        self.actor_obj = Actor()

    ###=======================================Success cases==================================###

    def test_create_actor(self):
        self.assertIsNotNone(self.actor_obj)
        self.assertIsInstance(self.actor_obj, Actor)

    def test_get_current_phrase(self):
        self.assertEqual(self.actor_obj.current_phrase, None)

    def test_set_phrase(self):
        self.actor_obj.set_phrase('test phrase')
        self.assertEqual(self.actor_obj.current_phrase, 'test phrase')
        self.assertEqual(self.actor_obj.current_phrase_word_list, ['test', 'phrase'])

    def test_get_current_word(self):
        self.assertEqual(self.actor_obj.current_word, None)

    def test_set_current_word(self):
        self.actor_obj.set_phrase('test phrase')
        self.actor_obj.set_word(1)
        self.assertEqual(self.actor_obj.current_word, 'phrase')

    def test_complete_word(self):
        self.actor_obj.set_phrase('test phrase')
        self.actor_obj.set_word(1)
        self.actor_obj.complete_word()
        self.assertEquals(self.actor_obj.completed_words, [1])

    def test_comp_word_resets_word(self):
        """
        Ensures that the complete_word function makes the current_word
        variable None after a successful completion.
        """
        self.actor_obj.set_phrase('test phrase')
        self.actor_obj.set_word(1)
        self.actor_obj.complete_word()
        self.assertIsNone(self.actor_obj.current_word)

    ###=======================================Failure cases==================================###

    def test_out_of_scope_set_word(self):
        self.actor_obj.set_phrase('test phrase')
        self.assertRaises(RuntimeError,
                          self.actor_obj.set_word,
                          2)

    def test_set_word_with_no_phrase(self):
        self.assertRaises(RuntimeError,
                          self.actor_obj.set_word,
                          1)

    def test_comp_word_no_phrase(self):
        self.assertRaises(RuntimeError,
                          self.actor_obj.complete_word)

    def test_comp_word_no_current_word(self):
        self.actor_obj.set_phrase('test phrase')
        self.assertRaises(RuntimeError,
                          self.actor_obj.complete_word)

    def test_set_word_already_complete(self):
        self.actor_obj.set_phrase('test phrase')
        self.actor_obj.set_word(1)
        self.actor_obj.complete_word()
        self.assertRaises(RuntimeError,
                          self.actor_obj.set_word,
                          1)

    def tearDown(self):
        del self.actor_obj
