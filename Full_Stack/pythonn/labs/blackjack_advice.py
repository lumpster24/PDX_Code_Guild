# blackjack_advice.py 6/29/18

# Reference: https://wizardofodds.com/blackjack/images/bj_4d_s17.gif

# initialize card values
card_values = {'J': 10, 'Q': 10, 'K': 10, 'A': [1, 11]}
for i in range(9):
    card_values['{}'.format(i + 2)] = i + 2


def print_hit():
    print("You should Hit.")


def print_stand():
    print("You should Stand.")


def print_double_hit():
    print("You should Double Down if allowed. Otherwise, Hit.")


def print_double_stand():
    print("You should Double Down if allowed. Otherwise, Stand.")


def print_split():
    print("You should Split.")


def print_split_hit():
    print("You should Split if Double Down after Split is allowed. "
          "Otherwise, Hit.")


def print_surrender_hit():
    print("You should Surrender if allowed. Otherwise, Hit.")


def print_blackjack():
    print("Blackjack!!!")


def print_bust():
    print("You Bust.")


def main():
    while True:
        # check if input is valid
        while True:
            first_card = input("What's your first card "
                               "(type done to quit)? ").upper()
            if first_card == 'DONE':
                print("Goodbye!")
                exit(0)
            if first_card not in card_values.keys():
                print("Invalid card value.")
            else:
                break

        while True:
            second_card = input("What's your second card "
                                "(type done to quit)? ").upper()
            if second_card == 'DONE':
                print("Goodbye!")
                exit(0)
            if second_card not in card_values.keys():
                print("Invalid card value.")
            else:
                break

        while True:
            dealer_card = input("What is the dealer showing "
                                "(type done to quit)? ").upper()
            if dealer_card == 'DONE':
                print("Goodbye!")
                exit(0)
            if dealer_card not in card_values.keys():
                print("Invalid card value.")
            else:
                break

        if dealer_card == 'A':
            dealer_card_value = card_values[dealer_card][1]
        else:
            dealer_card_value = card_values[dealer_card]

        # determine if 'A' should be 1 or 11
        if first_card != 'A' and second_card != 'A':
            soft_or_hard = 'hard'
            first_card_value = card_values[first_card]
            second_card_value = card_values[second_card]
        elif first_card == 'A' and second_card == 'A':
            print("You have a soft 12.")
            print("Dealer has {}".format(dealer_card_value))
            print_split()
            continue
        else:
            soft_or_hard = 'soft'
            if first_card == 'A':
                if card_values[first_card][1] + card_values[second_card] <= 21:
                    first_card_value = card_values[first_card][1]
                else:
                    first_card_value = card_values[first_card][0]
                second_card_value = card_values[second_card]
            if second_card == 'A':
                if card_values[first_card] + card_values[second_card][1] <= 21:
                    second_card_value = card_values[second_card][1]
                else:
                    second_card_value = card_values[second_card][0]
                first_card_value = card_values[first_card]

        print("You have a {} {}".format(soft_or_hard, first_card_value +
              second_card_value))
        print("Dealer has {}".format(dealer_card_value))

        # if first_card_value + second_card_value < 17:
        #     print_hit()
        # elif 17 < first_card_value + second_card_value < 21:
        #     print_stand
        # elif first_card_value + second_card_value == 21:
        #     print_blackjack()
        # elif first_card_value + second_card_value > 21:
        #     print_bust()

        if first_card_value + second_card_value == 21:
            print_blackjack()
            continue

        # pair values - both cards are the same
        if first_card_value == second_card_value:
            if first_card_value in [2, 3]:
                if dealer_card_value in [2, 3]:
                    print_split_hit()
                elif dealer_card_value in [4, 5, 6, 7]:
                    print_split()
                else:
                    print_hit()
            if first_card_value == 4:
                if dealer_card_value in [5, 6]:
                    print_split_hit()
                else:
                    print_hit()
            if first_card_value == 5:
                if dealer_card_value not in [10, 11]:
                    print_double_hit()
                else:
                    print_hit()
            if first_card_value == 6:
                if dealer_card_value in [2]:
                    print_split_hit()
                elif dealer_card_value in [3, 4, 5, 6]:
                    print_split()
                else:
                    print_hit()
            if first_card_value == 7:
                if dealer_card_value not in [8, 9, 10, 11]:
                    print_split()
                else:
                    print_hit()
            if first_card_value in [8]:
                print_split()
            if first_card_value == 9:
                if dealer_card_value not in [7, 10, 11]:
                    print_split()
                else:
                    print_stand()
            if first_card_value == 10:
                print_stand()

        # hard values - neither card is an ace
        elif first_card_value != 11 and second_card_value != 11:
            if 5 <= first_card_value + second_card_value <= 8:
                print_hit()
            if first_card_value + second_card_value == 9:
                if dealer_card_value in [3, 4, 5, 6]:
                    print_double_hit()
                else:
                    print_hit()
            if first_card_value + second_card_value in [10, 11]:
                if dealer_card_value not in [10, 11]:
                    print_double_hit()
                else:
                    print_hit()
            if first_card_value + second_card_value == 12:
                if dealer_card_value in [4, 5, 6]:
                    print_stand()
                else:
                    print_hit()
            if 13 <= first_card_value + second_card_value <= 16:
                if dealer_card_value in [2, 3, 4, 5, 6]:
                    print_stand()
                elif first_card_value + second_card_value == 15 \
                        and dealer_card_value in [10]:
                    print_surrender_hit()
                elif first_card_value + second_card_value == 16 \
                        and dealer_card_value in [9, 10, 11]:
                    print_surrender_hit()
                else:
                    print_hit()
            if 17 <= first_card_value + second_card_value <= 21:
                if first_card_value + second_card_value == 21:
                    print_blackjack()
                else:
                    print_stand()

        # soft values - at least one card is an ace
        elif first_card_value == 11 or second_card_value == 11:
            if first_card_value + second_card_value in [13, 14]:
                if dealer_card_value in [5, 6]:
                    print_double_hit()
                else:
                    print_hit()
            if first_card_value + second_card_value in [15, 16]:
                if dealer_card_value in [4, 5, 6]:
                    print_double_hit()
                else:
                    print_hit()
            if first_card_value + second_card_value in [17]:
                if dealer_card_value in [3, 4, 5, 6]:
                    print_double_hit()
                else:
                    print_hit()
            if first_card_value + second_card_value in [18]:
                if dealer_card_value in [3, 4, 5, 6]:
                    print_double_stand()
                elif dealer_card_value in [2, 7, 8]:
                    print_stand()
                else:
                    print_hit()
            if 19 <= first_card_value + second_card_value <= 21:
                print_stand()

main()
