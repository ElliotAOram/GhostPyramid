"""Testing module for game class"""
import unittest
from charades.actor import Actor
from charades.game import Game
from charades.viewer import Viewer

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

    def test_add_valid_viewer(self):
        self.assertTrue(self.game_obj.add_viewer(Viewer()))

    def test_add_max_actor(self):
        for _ in range(0, 6):
            self.assertTrue(self.game_obj.add_viewer(Viewer()))
        self.assertFalse(self.game_obj.add_viewer(Viewer()))

    ###=======================================Failure cases==================================###

    def tearDown(self):
        del self.game_obj
