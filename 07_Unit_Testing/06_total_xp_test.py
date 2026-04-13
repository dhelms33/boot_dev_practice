import unittest
from 06_total_xp import *

class TestXPPerPlayer(unittest.TestCase):
    def test_xp(self):
        #test areas when xp >= 0
        self.assertAlmostEqual(total_xp(3,300), 600)