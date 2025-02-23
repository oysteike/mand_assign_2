import unittest
import sys
import os

# Legg til src-mappen i søkestien
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../src')))

from HandOfCards import HandOfCards
from PlayingCard import PlayingCard

class TestHandOfCards(unittest.TestCase):
    def test_hand(self):
        #Sjekker at hånden er riktig
        cards = [PlayingCard('H', 1), PlayingCard('D', 5), PlayingCard('S', 10)]
        hand = HandOfCards(cards)
        self.assertEqual(len(hand.cards), 3)

    def test_is_flush(self):
        #Sjekker at is_flush() returnerer True for en flush
        flush_hand = HandOfCards([
            PlayingCard('H', 1), PlayingCard('H', 2), PlayingCard('H', 3), PlayingCard('H', 4), PlayingCard('H', 5)
        ])
        self.assertTrue(flush_hand.is_flush())

        #Sjekker at is_flush() returnerer False for en hånd som ikke er en flush
        non_flush_hand = HandOfCards([
            PlayingCard('H', 1), PlayingCard('D', 2), PlayingCard('H', 3), PlayingCard('S', 4), PlayingCard('H', 5)
        ])
        self.assertFalse(non_flush_hand.is_flush())

    def test_hand_string_representation(self):
        #Sjekker at __str__() returnerer en streng med alle kortene i hånden
        cards = [PlayingCard('H', 1), PlayingCard('D', 5), PlayingCard('S', 10)]
        hand = HandOfCards(cards)
        hand_str = str(hand)
        self.assertTrue(all(card.get_as_string() in hand_str for card in cards))

if __name__ == '__main__':
    unittest.main()