import unittest
import sys, os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))

try:
    from DeckOfCards import DeckOfCards
    from HandOfCards import HandOfCards
    print("Imports successful")  #Sjekker at man kan importe
except ImportError as e:
    print("ImportError:", e)

class TestDeckOfCards(unittest.TestCase):
    def test_deck(self): #Sjekker at man får 52 kort i en ny kortstokk 
        deck = DeckOfCards()
        print("Deck initialized") 
        self.assertEqual(len(deck.cards), 52, "Deck should contain 52 cards")
    
    def test_deal_hand(self): #Sjekker at man får riktig antall kort i en hånd
        deck = DeckOfCards()
        hand = deck.deal_hand(5)
        assert len(hand.cards) == 5, "Hand should contain 5 cards"

    def test_string_convert(self): #Sjekker at konvertering til streng går
        deck = DeckOfCards()
        self.assertEqual(str(deck), ', '.join(card.get_as_string() for card in deck.cards), "String conversion failed")

if __name__ == '__main__':
    unittest.main()