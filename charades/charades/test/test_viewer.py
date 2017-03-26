"""Testing module for viewer class"""
import unittest
from charades.viewer import Viewer

class TestViewer(unittest.TestCase):
    """
    Tests the ViewerClass for basic interactions
    """

    def setUp(self):
        self.viewer_obj = Viewer()

    def test_create_viewer(self):
        self.assertIsNotNone(self.viewer_obj)
        self.assertIsInstance(self.viewer_obj, Viewer)

    def test_get_points(self):
        self.assertEqual(self.viewer_obj.points, 0)

    def test_increment_points(self):
        self.viewer_obj.increment_points(25)
        self.assertEqual(self.viewer_obj.points, 25)

        self.viewer_obj.increment_points(10)
        self.assertEqual(self.viewer_obj.points, 35)

    def test_get_name(self):
        self.assertEqual(self.viewer_obj.name, 'anonymous')

    def test_set_name(self):
        self.viewer_obj.set_name('test-name')
        self.assertEqual(self.viewer_obj.name, 'test-name')

    def tearDown(self):
        del self.viewer_obj
