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
        self.actor_obj.set_phrase('test phrase', 'test genre')
        self.assertEqual(self.actor_obj.current_phrase, 'test phrase')
        self.assertEqual(self.actor_obj.current_phrase_word_list, ['test', 'phrase'])
        self.assertEqual(self.actor_obj.phrase_genre, 'test genre')

    def test_get_current_word(self):
        self.assertEqual(self.actor_obj.current_word, None)

    def test_set_current_word(self):
        self.actor_obj.set_phrase('test phrase', 'test genre')
        self.actor_obj.set_word(1)
        self.assertEqual(self.actor_obj.current_word, 'phrase')

    def test_complete_word(self):
        self.actor_obj.set_phrase('test phrase', 'test genre')
        self.actor_obj.set_word(1)
        self.actor_obj.complete_word()
        self.assertEquals(self.actor_obj.completed_words, [1])

    def test_comp_word_resets_word(self):
        """
        Ensures that the complete_word function makes the current_word
        variable None after a successful completion.
        """
        self.actor_obj.set_phrase('test phrase', 'test genre')
        self.actor_obj.set_word(1)
        self.actor_obj.complete_word()
        self.assertIsNone(self.actor_obj.current_word)

    def test_phrase_ready_single_true(self):
        """
        Ensure that true is return for valid single word state
        """
        self.actor_obj.set_phrase('test', 'test genre')
        self.assertTrue(self.actor_obj.phrase_ready())

    def test_phrase_ready_multi_true(self):
        """
        Ensures that true is returned for valid multiword state
        """
        self.actor_obj.set_phrase('test phrase', 'test genre')
        self.actor_obj.set_word(0)
        self.assertTrue(self.actor_obj.phrase_ready())

    def test_phrase_complete(self):
        """
        Ensure all variables are reset after phrase complete
        """
        self.actor_obj.set_phrase('test phrase', 'test genre')
        self.actor_obj.set_word(0)
        self.actor_obj.complete_word()
        self.actor_obj.set_word(1)
        self.assertEqual(self.actor_obj.completed_words, [0])
        self.assertEqual(self.actor_obj.current_word_index, 1)
        self.actor_obj.phrase_complete()
        self.assertEqual(self.actor_obj.current_phrase, None)
        self.assertEqual(self.actor_obj.current_phrase_word_list, None)
        self.assertEqual(self.actor_obj.current_word, None)
        self.assertEqual(self.actor_obj.current_word_index, None)
        self.assertEqual(self.actor_obj.completed_words, [])
        self.assertEqual(self.actor_obj.phrase_genre, None)


    ###=======================================Failure cases==================================###

    def test_out_of_scope_set_word(self):
        self.actor_obj.set_phrase('test phrase', 'test genre')
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
        self.actor_obj.set_phrase('test phrase', 'test genre')
        self.assertRaises(RuntimeError,
                          self.actor_obj.complete_word)

    def test_set_word_already_complete(self):
        self.actor_obj.set_phrase('test phrase', 'test genre')
        self.actor_obj.set_word(1)
        self.actor_obj.complete_word()
        self.assertRaises(RuntimeError,
                          self.actor_obj.set_word,
                          1)

    def test_phrase_ready_no_phrase(self):
        """
        Ensures false is returned with no phrase selected
        """
        self.assertFalse(self.actor_obj.phrase_ready())

    def test_phrase_ready_no_word(self):
        """
        Ensure false is returned with no word selected from phrase
        """
        self.actor_obj.set_phrase('test phrase', 'test genre')
        self.assertFalse(self.actor_obj.phrase_ready())

    def test_phrase_ready_no_word_index(self):
        """
        Ensure false is returned with no current_word_index
        (should not be a reachable state but is being checked for clarity)
        """
        self.actor_obj.set_phrase('test phrase', 'test genre')
        self.actor_obj.current_word = 'test'
        self.assertFalse(self.actor_obj.phrase_ready())

    def tearDown(self):
        del self.actor_obj
