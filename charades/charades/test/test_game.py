"""Testing module for game class"""
import unittest
from charades.actor import Actor
from charades.game import Game

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
        self.assertEqual(viewer.viewer_number, 1)

    def test_lookup_invalid_viewer(self):
        viewer_num = self.game_obj.add_viewer()
        self.assertFalse(self.game_obj.lookup_viewer(2))

    ###=======================================Failure cases==================================###

    def tearDown(self):
        del self.game_obj
