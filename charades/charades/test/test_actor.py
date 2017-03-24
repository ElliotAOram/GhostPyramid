"""Testing module for actor class"""
import unittest
from charades import actor

class TestActor(unittest.TestCase):

    def setUp(self):
        self.actor_obj = Actor()

    def test_create_actor(self):
        self.assertIsNotNone(self.actor_obj)
        self.assertIsInstance(self.actor_obj, type(Actor))

    def test_get_current_phrase(self):
        self.assertEqual(self.actor_obj.current_phrase, '')

    def test_set_phrase(self):
        self.actor_obj.set_phrase('test phrase')
        self.assertEqual(self.actor_obj.current_phrase, 'test phrase')

    def test_get_current_word(self):
        self.assertEqual(actor_obj.current_word, None)

    def test_set_current_word(self):
        self.actor_obj.set_phrase('test phrase')
        actor_obj.set_current_word(1)
        self.assertEqual(actor_obj.current_word, 'phrase')

    def test_complete_word(self):
        self.actor_obj.set_phrase('test phrase')
        actor_obj.complete_word(1)
        self.assertEquals(actor_obj.complted_words, [1])

    def test_duplicate_completed_word(self):
        self.actor_obj.set_phrase('test phrase')
        actor_obj.complete_word(1)
        actor_obj.complete_word(1)
        self.assertEquals(actor_obj.complted_words, [1])

    def test_out_of_scope_completed_word(self):
        self.actor_obj.set_phrase('test phrase')
        self.assertRaises(RuntimeError,
                          actor_obj.complete_word,
                          2)

    def tearDown(self):
        self.actor_obj = None
