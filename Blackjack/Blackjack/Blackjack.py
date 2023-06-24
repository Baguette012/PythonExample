import random
# FIRST SECTION INSERT YOUR CODE HERE
suits = ['clubs', 'diamonds', 'hearts', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
deck = [(suit, rank) for suit in suits for rank in ranks]

# print (deck)

player = []
dealer = []

def draw_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card
# print(draw_card(deck))

def deal(deck, player, dealer):
    for i in range(2):
        player_card = draw_card(deck)
        dealer_card = draw_card(deck)

        player.append(player_card)
        dealer.append(dealer_card)
        
deal(deck, player, dealer)

#print("Player's hand:", player)
#print("Dealer's hand:", dealer[0])

def get_count(player):
    count = 0
    for card in player:
        rank = card[1]
        if rank == '11' or rank == '12' or rank == '13': # logic for face cards
            count += 10
        elif rank == '14': # ace logic
            count += 11
        else:
            count += int(rank)
    return count
 
#print ("Player ",get_count(player))
#print ("Dealer ",get_count(dealer))

def check_cards(player, dealer):
    player_total = get_count(player)
    dealer_total = get_count(dealer)
    
    if player_total == 21:
        return 'WIN'
    elif dealer_total == 21:
        return 'BUST'
    elif player_total > 21:
        return 'BUST'
    elif player_total < dealer_total:
        return 'BUST'
    elif player_total > dealer_total:
        return 'WIN'
    else:
        return 'how'


    # second SECTION INSERT YOUR CODE HERE


def create_blackjack_game(player, dealer, deck):
    while True:
        print("Player's hand:")
        for card in player:
            print(card)
        print("Dealer's hand:")
        for card in dealer:
            print(card)
        
        response = input("Enter 'h' to hit, 's' to stand, or 'q' to quit: ")
        
        if response == 'q':
            exit()  # Quit the game
            
        if response == 'h': #hit
            player.append(draw_card(deck))
            if get_count(player) > 21:
                print("Player's hand:")
                for card in player:
                    print(card)
                print("Dealer's hand:")
                for card in dealer:
                    print(card)
                print("Player busts, dealer wins!")
                return 'BUST'
            
        if response == 's': # stand
            while get_count(dealer) < 17:
                dealer.append(draw_card(deck))
            return check_cards(player, dealer)

     # THIRD SECTION INSERT YOUR CODE HERE
        #def dealer_turn(deck, player, dealer):    didnt use 
#    while get_count(dealer) < 17:
#        dealer.append(draw_card(deck))
#        print("Dealer draws a card:")
#        print(dealer)
#        if get_count(dealer) > 21:
#            print("Dealer busts, player wins!")
#            return 'WIN'
#    if get_count(player) > get_count(dealer):
#        return 'WIN'
#    elif get_count(player) < get_count(dealer):
#        return 'BUST'
#    else:
#        return 'OK'


#calling game and winner format
result = create_blackjack_game(player, dealer, deck)
print("Result: ", result)
print("Player's final hand:")
for card in player:
    print(card)
print("Dealer's final hand:")
for card in dealer:
    print(card)
print("Result: ", result)