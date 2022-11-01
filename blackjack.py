# A blackjack game created by George Akanimoh
# Gamble responsibly. This game in no way supports gambling.
import random

def get_random_char(list):
    # get length of list
    list_len = len(list)

    # if no characters are left return -1
    if len(list) == 0:
        return -1
    
    # select random character 
    rand_index = random.randrange(list_len)
    rand_char = list[rand_index]
    # remove character from array
    list[rand_index] = list[list_len - 1]
    list[list_len - 1] = None

    # return character 
    return rand_char

def card_counter_dealer(string):
    value = 0
    if string == "K" or string == "Q" or string == "J":
        value += 10
    elif string == "A":
        value += 11
    else:
        value += int(string)
    
    return value

def card_counter_player(string):
    value = 0
    if string == "K" or string == "Q" or string == "J":
        value += 10
    # player to choose value of ace
    elif string == "A":
        value += int(input("Enter your choice for the ace: 1 or 11. "))
    else:
        value += int(string)

    return value

def hit_or_stand():
    return (input("Choose H to hit or S to stand: "))

def card_value_check(dealer_cards, player_cards):
    if dealer_cards == player_cards == 21:
        return "Draw!"
    elif player_cards < dealer_cards == 21:
        return "Dealer blackjack"
    elif dealer_cards < player_cards == 21:
        return "Player blackjack"
    elif 21 > player_cards > dealer_cards:
        return "You win!"
    elif 21 > dealer_cards > player_cards:
        return "House wins"
    elif player_cards < 21 < dealer_cards:
        return "You win!" 
    elif player_cards == 21 < dealer_cards:
        return "Player blackjack" 
    elif player_cards == dealer_cards > 21:
        return "House wins"
    elif player_cards == dealer_cards < 21:
        return "Draw"
    
def main():
    print("======== Welcome to Nemo BlackJack ========")
    deck = ["A", "A", "A", "A", "2", "2", "2", "2", "3", "3","3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "J", "J", "J", "J", "K", "K", "K", "K", "Q", "Q", "Q", "Q"]
    player_cards = []   # holds player's cards
    dealer_cards = []   # holds dealer's cards
    player_card_count = 0
    dealer_card_count = 0

    # deal cards to dealer and player
    dealer_cards.append(get_random_char(deck))
    player_cards.append(get_random_char(deck))
    dealer_cards.append(get_random_char(deck))
    player_cards.append(get_random_char(deck))

    # check for None type value
    for i in range(2):
        # replace with other value if found
        while dealer_cards[i] == None:
            dealer_cards[i] = get_random_char(deck)
        while player_cards[i] == None:
            player_cards[i] = get_random_char(deck)

    # show cards
    print("Your cards are [" + player_cards[0] + " and " + player_cards[1] + "].")
    print("The dealer's cards are [" + dealer_cards[0] + "]." )

    # add values of cards
    for i in range(2):
        # dealer_card_count += card_counter_dealer(dealer_cards[i])
        player_card_count += card_counter_player(player_cards[i])
    
    dealer_card_count += card_counter_dealer(dealer_cards[0])

    # player choices
    player_choice = hit_or_stand()
    while player_choice == "H" or player_choice == "h":
        player_cards.append(get_random_char(deck))
        list_len_p = len(player_cards)
        while player_cards[list_len_p - 1] == None:
            player_cards[list_len_p - 1] = get_random_char(deck)
        player_card_count += card_counter_player(player_cards[list_len_p - 1])
        print("Your cards are ", player_cards)
        if player_card_count > 21:
            print("Bust! You lose")
            return
        player_choice = hit_or_stand()
    else:
        player_card_count += 0

    # show player card value
    print("Your cards are ", player_cards)
    print("The value of your cards are: " + str(player_card_count))

    # add hole card
    dealer_card_count += card_counter_dealer(dealer_cards[1])
    print("Hole card is " + dealer_cards[1])        
    # dealer hits. using H17
    while dealer_card_count <= 17:
        dealer_cards.append(get_random_char(deck))
        list_len_d = len(dealer_cards)
        while dealer_cards[list_len_d - 1] == None:
            dealer_cards[list_len_d - 1] = get_random_char(deck)
        dealer_card_count += card_counter_dealer(dealer_cards[list_len_d - 1])
        print("Dealer just picked " + dealer_cards[list_len_d -1])
        print("Dealer's cards are ", dealer_cards)
    
    # compare with player cards
    print(card_value_check(dealer_card_count, player_card_count))

    print("Dealer card value is " + str(dealer_card_count))
    print("Player card value is " + str(player_card_count))

main()