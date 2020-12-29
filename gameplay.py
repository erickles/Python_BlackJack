from hand import Hand
from deck import Deck
from chips import Chips

def take_bet(chips):

    while True:

        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Sorry, please provide an integer')
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips! You have {}'.format(chips.total))
            else:
                break

def hit(deck, hand):
    single_card = deck.deal()    
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing # to control an upcoming loop

    while True:
        x = input('Hit or Stand? Enter h or s')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands Dealer's turn")
            playing = False
        else:
            print("Sorry, I did no understand that, Please enter h or s only!")
            continue

def player_busts(player, dealer, chips):
    print('Bust Player!')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Player Wins!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('Player Wins! Dealer Busted')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('Dealer Wins!')
    chips.lose_bet()

def push(player, dealer):
    print('Dealer and Player tie! PUSH')

def show_some(player, dealer):
    print('Dealers Hand')
    print('One car hidden')
    print(dealer.cards[1])
    print('\n')
    print('Player Hand:')

    for card in player.cards:
        print(card)

def show_all(player, dealer):
    print('Dealers hand:')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('Players Hand')
    for card in player.cards:
        print(card)

while True:
    
    # Print an opening statement
    print('Welcome to Black Jack')

    # Create & Shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    
    while playing: # recall this variable from our hit_or_stand function
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        # Show all cards
        show_all(player_hand, dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            dealer_busts(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # Inform Player of their chips total
    print('\n Player total chips are at: {}'.format(player_chips.total))
    # Ask to play again
    new_game = input('Would you like to play another hand? y/n')
    if new_game[0].lower() == 'y':
        playing = True
    else:
        print('Thank you for playing')
        break

