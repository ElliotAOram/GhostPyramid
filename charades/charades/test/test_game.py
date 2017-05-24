"""Testing module for game class"""
import unittest
from charades.model.actor import Actor
from charades.model.game import Game

#pylint: disable=too-many-public-methods
class TestGame(unittest.TestCase):
    """
    Tests for the game.py Actor class
    """

    def setUp(self):
        self.game_obj = Game()

    ###=======================================Success cases==================================###

    def test_create_game(self):
        self.assertIsNotNone(self.game_obj)
        self.assertIsInstance(self.game_obj, Game)
        self.assertEqual(self.game_obj.viewers, [])

    def test_add_valid_actor(self):
        self.assertTrue(self.game_obj.add_actor(Actor()))

    def test_add_second_actor(self):
        self.assertTrue(self.game_obj.add_actor(Actor()))
        self.assertFalse(self.game_obj.add_actor(Actor()))

    def test_add_viewer(self):
        self.assertEqual(1, self.game_obj.add_viewer())

    def test_add_max_actor(self):
        for i in range(0, 6):
            self.assertEqual(i + 1, self.game_obj.add_viewer())
        self.assertFalse(self.game_obj.add_viewer())

    def test_lookup_valid_viewer(self):
        viewer_num = self.game_obj.add_viewer()
        viewer = self.game_obj.lookup_viewer(1)
        self.assertEqual(viewer.viewer_number, viewer_num)

    def test_lookup_invalid_viewer(self):
        self.game_obj.add_viewer()
        self.assertRaises(RuntimeError,
                          self.game_obj.lookup_viewer,
                          2)

    def test_set_guess_type(self):
        self.game_obj.set_guess_type(True)
        self.assertEqual(self.game_obj.current_correct_guess_type, 'Phrase')
        self.game_obj.set_guess_type(False)
        self.assertEqual(self.game_obj.current_correct_guess_type, 'Word')

    def test_set_guess_type_non_bool(self):
        self.assertFalse(self.game_obj.set_guess_type('String'))

    def test_set_guess_word(self):
        self.game_obj.add_actor(Actor())
        self.game_obj.actor.set_phrase('test', 'test genre')
        self.game_obj.set_guess_type(True)
        self.game_obj.set_guess('test')
        self.assertEqual(self.game_obj.current_correct_guess, 'test')

    def test_set_guess_word_no_type(self):
        self.game_obj.add_actor(Actor())
        self.game_obj.actor.set_phrase('test', 'test genre')
        self.game_obj.set_guess('test')
        self.assertEqual(self.game_obj.current_correct_guess, 'test')
        self.assertEqual(self.game_obj.current_correct_guess_type, 'Word')

    def test_set_guess_word_incorrect(self):
        self.game_obj.add_actor(Actor())
        self.game_obj.actor.set_phrase('test', 'test genre')
        self.game_obj.set_guess_type(True)
        self.assertFalse(self.game_obj.set_guess('wrong'))
        self.assertIsNone(self.game_obj.current_correct_guess)

    def test_set_guess_phrase(self):
        self.game_obj.add_actor(Actor())
        self.game_obj.actor.set_phrase('test phrase', 'test genre')
        self.game_obj.set_guess_type(True)
        self.game_obj.set_guess('test phrase')
        self.assertEqual(self.game_obj.current_correct_guess, 'test phrase')

    def test_set_guess_word_in_phrase(self):
        self.game_obj.add_actor(Actor())
        self.game_obj.actor.set_phrase('test phrase', 'test genre')
        self.game_obj.actor.set_word(1)
        self.game_obj.set_guess_type(False)
        self.game_obj.set_guess('phrase')
        self.assertEqual(self.game_obj.current_correct_guess, 'phrase')
        self.assertEqual(self.game_obj.current_correct_guess_type, 'Word')

    def test_set_guess_phrase_no_type(self):
        self.game_obj.add_actor(Actor())
        self.game_obj.actor.set_phrase('test phrase', 'test genre')
        self.game_obj.set_guess('test phrase')
        self.assertEqual(self.game_obj.current_correct_guess, 'test phrase')
        self.assertEqual(self.game_obj.current_correct_guess_type, 'Phrase')

    def test_set_guess_incorrect_phrase(self):
        self.game_obj.add_actor(Actor())
        self.game_obj.actor.set_phrase('test phrase', 'test genre')
        self.game_obj.set_guess_type(True)
        self.assertFalse(self.game_obj.set_guess('incorrect guess'))
        self.assertIsNone(self.game_obj.current_correct_guess)

    def test_reset_guess_state(self):
        self.game_obj.current_correct_guess = 'test'
        self.game_obj.current_correct_guess_type = 'Word'
        self.game_obj.reset_guess_state()
        self.assertIsNone(self.game_obj.current_correct_guess)
        self.assertIsNone(self.game_obj.current_correct_guess_type)

    def add_viewers(self, num_viewers):
        for _ in range(0, num_viewers):
            self.game_obj.add_viewer()

    def test_get_position_first(self):
        self.add_viewers(2)
        position_1 = self.game_obj.get_viewer_position(1)
        position_2 = self.game_obj.get_viewer_position(2)
        self.assertEqual(position_1, '1st')
        self.assertEqual(position_2, '1st')

    def test_get_position_second(self):
        self.add_viewers(2)
        self.game_obj.lookup_viewer(1).increment_points(10)
        position_1 = self.game_obj.get_viewer_position(1)
        position_2 = self.game_obj.get_viewer_position(2)
        self.assertEqual(position_1, '1st')
        self.assertEqual(position_2, '2nd')

    def test_get_position_third(self):
        self.add_viewers(3)
        self.game_obj.lookup_viewer(1).increment_points(20)
        self.game_obj.lookup_viewer(2).increment_points(10)
        position_3 = self.game_obj.get_viewer_position(3)
        self.assertEqual(position_3, '3rd')

    def test_get_position_forth(self):
        self.add_viewers(4)
        self.game_obj.lookup_viewer(1).increment_points(30)
        self.game_obj.lookup_viewer(2).increment_points(20)
        self.game_obj.lookup_viewer(3).increment_points(10)
        position_4 = self.game_obj.get_viewer_position(4)
        self.assertEqual(position_4, '4th')



    def tearDown(self):
        del self.game_obj
