import random
from collections import deque

class Card:
    """Represents a playing card."""
    
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.RANKS.index(rank)
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    """Represents a deck of cards."""
    
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, num_players):
        hands = [deque() for _ in range(num_players)]
        for i, card in enumerate(self.cards):
            hands[i % num_players].append(card)
        return hands

class WarGame:
    """Implements the War card game."""
    
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand, self.computer_hand = self.deck.deal(2)
        self.round_num = 0
        self.max_rounds = 1000  # Prevent infinite games
    
    def play_round(self):
        """Play a single round of War."""
        self.round_num += 1
        
        # Check if either player has run out of cards
        if not self.player_hand or not self.computer_hand:
            return True
        
        print(f"\nRound {self.round_num}:")
        print(f"Player cards: {len(self.player_hand)}, Computer cards: {len(self.computer_hand)}")
        
        # Draw cards
        player_card = self.player_hand.popleft()
        computer_card = self.computer_hand.popleft()
        
        print(f"Player drew: {player_card}")
        print(f"Computer drew: {computer_card}")
        
        # Cards in the current battle
        cards_in_play = [player_card, computer_card]
        
        # Compare cards
        while player_card.value == computer_card.value:
            print("WAR!")
            
            # Check if either player has insufficient cards for war
            if len(self.player_hand) < 4 or len(self.computer_hand) < 4:
                # Player with more cards wins
                if len(self.player_hand) > len(self.computer_hand):
                    self.player_hand.extend(cards_in_play)
                    print("Player wins the war (opponent has insufficient cards)!")
                else:
                    self.computer_hand.extend(cards_in_play)
                    print("Computer wins the war (opponent has insufficient cards)!")
                return False
            
            # Each player places 3 cards face down
            for _ in range(3):
                cards_in_play.append(self.player_hand.popleft())
                cards_in_play.append(self.computer_hand.popleft())
            
            # Each player turns up a card
            player_card = self.player_hand.popleft()
            computer_card = self.computer_hand.popleft()
            cards_in_play.extend([player_card, computer_card])
            
            print(f"Player drew: {player_card}")
            print(f"Computer drew: {computer_card}")
        
        # Determine winner of the round
        if player_card.value > computer_card.value:
            self.player_hand.extend(cards_in_play)
            print("Player wins the round!")
        else:
            self.computer_hand.extend(cards_in_play)
            print("Computer wins the round!")
        
        return False
    
    def play_game(self):
        """Play the entire game of War."""
        game_over = False
        
        while not game_over and self.round_num < self.max_rounds:
            game_over = self.play_round()
            
            # Pause between rounds (uncomment for interactive play)
            # input("Press Enter to continue...")
        
        # Determine the winner
        print("\nGame Over!")
        if len(self.player_hand) > len(self.computer_hand):
            print("Player wins the game!")
        elif len(self.computer_hand) > len(self.player_hand):
            print("Computer wins the game!")
        else:
            print("The game is a tie!")
        
        print(f"Final score - Player: {len(self.player_hand)}, Computer: {len(self.computer_hand)}")
        
        if self.round_num >= self.max_rounds:
            print(f"Game ended after maximum rounds ({self.max_rounds}).")

if __name__ == "__main__":
    print("Welcome to the War Card Game!")
    game = WarGame()
    game.play_game()