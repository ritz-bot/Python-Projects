mport random
import os
from art import logogo
print(logogo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card =random.choice(cards)
    return card

print(deal_card())
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

def clear_screen():
    # Clear the screen based on the operating system
    if os.name == 'nt':  # for Windows
        _ = os.system('cls')
    else:  # for Mac and Linux (here, 'posix' is used)
        _ = os.system('clear')
def calculate_score(cards):
    """takes a list of cards and return the score calculated from cards"""
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    
    if sum(cards)==21 and len(cards)==2:
        return 0    
    
#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    
    
    

    return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have 
# the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), 
# then the user wins. If the user_score is over 21, then the user loses.
# If the computer_score is over 21, then the computer loses. If none of the above, 
# then the player with the highest score wins.


def compare(user_score, computer_score):
    if user_score==computer_score:
        return f'Draw 🙃'
    elif computer_score==0:
        return "Lose , opponent has a blackjack😱"
    elif user_score==0:
        return "win with a blackjack 😎"
    elif user_score >21:
        return "Game over. You lose!😭"
    elif computer_score > 21:
        return "oppone went over. You win😁"
    elif user_score > computer_score:
        return "You win😄"
    else:
        return "you loose"
    
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over=False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f'Your cards: {user_cards}, current_score:{ user_score}')
        print(f'Computer#s first cards: {computer_cards[0]} ')

        if user_score==0 or computer_score==0 or user_score > 21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True

    while computer_score!=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)


    print(f' Your final hand:{user_cards}, final_score={ user_score}' )
    print(f' Computer final hand:{computer_cards}, final_score={ computer_score}' )

    print(compare(user_score, computer_score))


    #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
    #and returns the score. 


    #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.



    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    



while input('Would you like to continue playiong game: Type Y or n: ')=='y':
    clear_screen()
    play_game()



#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and 
# start a new game of blackjack and show the logo from art.py.


