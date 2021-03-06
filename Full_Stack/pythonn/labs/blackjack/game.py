# game.py 7/9/18

from card import Card
from deck import Deck
from player import Player
from dealer import Dealer
from time import sleep
import os


class Game(object):
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

        # add two cards to the player hand, and dealer hand
        self.player = Player()
        self.dealer = Dealer()
        for i in range(2):
            self.player.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal())

    # clear terminal screen and keep print statement at the top
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to Blackjack!")

    # give player a card from the top of the deck
    def hit(self):
        self.player.add_card(self.deck.deal())

    # check if the person's score is over 21
    def bust(self, person):
        if person.score() > 21:
            return True
        return False

    # print the player and dealer's cards/score
    def print_game(self, stay=False):
        self.clear()
        print("---------")
        # if the player has not stayed we still need to hide
        # one of the dealer's cards
        if not stay:
            print("Dealer Showing (One Card is hidden):\n" +
                  self.dealer.visible_card())
            print("Points visible: " + self.dealer.visible_score())
        # once the player stays we can reveal all of the dealer's cards
        else:
            print("Dealer:\n" + str(self.dealer))
            print("Points: " + str(self.dealer.score()))
        print()
        print("Player:\n" + str(self.player))
        print("Points: " + str(self.player.score()))

    def repl(self):
        stay = False
        self.print_game(stay)  # print initial state of the game
        while True:
            command = input("Do you want to (h)it or (s)tay? ").lower()
            if command in ['hit', 'h']:
                self.hit()
                sleep(1.5)
                self.print_game(stay)
            elif command in ['stay', 's']:
                stay = True
            else:
                print("Invalid input.")
                continue

            # check if game over
            if self.bust(self.player):
                print("\nSorry. You lose.\n")
                break

            # if the player stays then it's the dealers turn
            if stay:
                # print the dealers hidden card and total score
                sleep(1.5)
                self.print_game(stay)
                while True:
                    if self.dealer.score() < 17:
                        self.dealer.add_card(self.deck.deal())
                        sleep(1.5)
                        self.print_game(stay)
                    else:
                        break

                # check if game over
                if self.bust(self.dealer) or \
                   self.player.score() > self.dealer.score():
                    print("\nYou win!\n")
                    break
                elif self.player.score() == self.dealer.score():
                    print("\nPush.\n")
                    break
                else:
                    print("\nSorry. You lose.\n")
                    break

if __name__ == '__main__':
    while True:
        print("--- New Round ---")
        newGame = Game()
        newGame.repl()

        while True:
            again = input("Would you like to play again? ").lower()
            if again in ['y', 'yes']:
                break
            elif again in ['n', 'no']:
                print("Thanks for playing!")
                exit(0)
            else:
                print("Invalid command.")
