# Exercise 11 - Vanessa Belous

import random
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

# Class to make Deck Object (Section 11.5 Code)
class Deck:
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    def deal(self):
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print('Reshuffling...!!!')
        self.current_card += 1
        return self.card_list[self.current_card - 1]

# Function 1 - creates a hand
def create_a_deck():
    global ranks, suits
    my_deck = Deck(52)
    card_no = 1
    hand = []

    # pull five cards
    for i in range(5):
        d = my_deck.deal()
        r = d % 13
        s = d // 13
        print('\t', card_no, '->', ranks[r], 'of', suits[s])
        card_no += 1
        # add card to hand list
        hand.append([ranks[r], suits[s]])

    return my_deck, hand

# Function 2 - replaces cards user specifies
def replace_cards(my_deck, hand, to_replace):
    global ranks, suits
    # split user response by delimiter into a list
    replace = to_replace.split(',')
    # string -> int
    replace = [int(num) for num in replace]
    # subtract 1 from every value to easily use them to traverse hand list
    replace = [(num - 1) for num in replace]

    # replace cards
    for index in replace:
        d = my_deck.deal()
        r = d % 13
        s = d // 13
        hand[index] = [ranks[r], suits[s]]

    # display new hand
    print("\nYour New Hand:")
    card_no = 1
    for card in hand:
        print('\t', card_no, '->', card[0], 'of', card[1])
        card_no += 1

def main():
    # create unique hand
    print("Your Hand:")
    my_deck, hand = create_a_deck()
    # ask user which cards they want to replace
    to_replace = input("\nWhich cards would you like replaced? (ex: 1, 3, 5): ")
    # run function to replace those cards
    replace_cards(my_deck, hand, to_replace)

main()