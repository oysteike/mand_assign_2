import unittest
import sys, os

# Add the parent directory of 'notebooks' to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))


from PlayingCard import PlayingCard

class TestPlayingCard(unittest.TestCase):
    def test_card_initialization(self):
        # Test at kortet initialiseres riktig
        card = PlayingCard('H', 1)
        assert card.get_suit() == 'H', "Suit should be 'H'"
        assert card.get_face() == 1, "Face value should be 1"

if __name__ == '__main__':
    unittest.main()