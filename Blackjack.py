import random
import time


def clear_page():
    print('\n' * 40)
    print(""" 
     /$$$$$$$  /$$        /$$$$$$   /$$$$$$  /$$   /$$    /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$
    | $$__  $$| $$       /$$__  $$ /$$__  $$| $$  /$$/   |__  $$ /$$__  $$ /$$__  $$| $$  /$$/
    | $$  \ $$| $$      | $$  \ $$| $$  \__/| $$ /$$/       | $$| $$  \ $$| $$  \__/| $$ /$$/ 
    | $$$$$$$ | $$      | $$$$$$$$| $$      | $$$$$/        | $$| $$$$$$$$| $$      | $$$$$/  
    | $$__  $$| $$      | $$__  $$| $$      | $$  $$   /$$  | $$| $$__  $$| $$      | $$  $$  
    | $$  \ $$| $$      | $$  | $$| $$    $$| $$\  $$ | $$  | $$| $$  | $$| $$    $$| $$\  $$ 
    | $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/| $$ \  $$|  $$$$$$/| $$  | $$|  $$$$$$/| $$ \  $$
    |_______/ |________/|__/  |__/ \______/ |__/  \__/ \______/ |__/  |__/ \______/ |__/  \__/                
                          """)
                          
                          
def blackjack_logo():
    print(""" 
 /$$$$$$$  /$$        /$$$$$$   /$$$$$$  /$$   /$$    /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$
| $$__  $$| $$       /$$__  $$ /$$__  $$| $$  /$$/   |__  $$ /$$__  $$ /$$__  $$| $$  /$$/
| $$  \ $$| $$      | $$  \ $$| $$  \__/| $$ /$$/       | $$| $$  \ $$| $$  \__/| $$ /$$/ 
| $$$$$$$ | $$      | $$$$$$$$| $$      | $$$$$/        | $$| $$$$$$$$| $$      | $$$$$/  
| $$__  $$| $$      | $$__  $$| $$      | $$  $$   /$$  | $$| $$__  $$| $$      | $$  $$  
| $$  \ $$| $$      | $$  | $$| $$    $$| $$\  $$ | $$  | $$| $$  | $$| $$    $$| $$\  $$ 
| $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/| $$ \  $$|  $$$$$$/| $$  | $$|  $$$$$$/| $$ \  $$
|_______/ |________/|__/  |__/ \______/ |__/  \__/ \______/ |__/  |__/ \______/ |__/  \__/                
                      """)
money = 2500


def bet_calculator(money):
    bet = int(input(f"     You Have £{money}, How Much Would You Like To Put Down: "))
    while bet <0 or bet > money:
        bet = int(input(f"        Please Bet an Appropriate Amount: "))
    money -= bet
    return bet, money #Returns how much was bet, and how much they have left
    
    
def initial_card_selector(deck):
    '''This Works out the first 2 cards delt, it is called for both the User and Computer giving a different output both times'''
    pictures = []
    values = []
    for i in range(0,2): #It chooses a random card from the Deck, and assigns its value and picture accordingly. Does it Twice
        choice = random.choice(deck)
        values.append(choice["value"])
        pictures.append(choice["art"])
    return pictures, values #returns a list of pictures and their corresponding values
    
    
def extra_card_selector(cards, deck):
    '''If Player chooses Hit, this finds the extra card they receive'''
    pictures = cards[0]
    values = cards[1]
    choice = random.choice(deck)
    values.append(choice["value"])
    pictures.append(choice["art"])
    return pictures, values
    
    
def card_shower(cards, i):
    pictures = cards[0] #This retrives the pictures and values of the cards
    values = cards[1]
    if i == 1:
        print("\nYour Cards Are: ")
    elif i==2:
        print("The Computers Cards Are: ")
    if i == 3:
        print("\nYour Cards Were: ")
    elif i == 4:
        print("The Computers Cards Were: ")
    time.sleep(1)
    for card in range(0, len(values)):
        if i == 1 or i == 3 or i == 4:
            print(pictures[card])
        elif i == 2 and card!=0: #Only the first card of the Computer should printed on the first iteration
            print(HIDDEN_CARD)
        else:
            print(pictures[card])
        time.sleep(0.3)


    total_value = 0 #Works out the Total Value of the Cards
    for k in range(0, len(values)):
        total_value += values[k]
    if 11 in values:
        if total_value > 21:
            total_value -=10
    return total_value, values #Returns the Total Value, and the Value list for adaptation
    
    
def computer_hit(total_comp_value):
    '''If computer value < 13, this function assigns a random chance for it to Hit'''
    randomizer = random.randint(0,1)
    if randomizer == 0:
        create = card_shower(extra_card_selector(comp_cards, DECK), 4)
        values = create[1]
        total_comp_value = create[0]
    else:
        card_shower(comp_cards, 4)
    return total_comp_value
    
    
def end_output(total_comp_value):
    clear_page()
    card_shower(user_cards, 3)
    if total_comp_value < 13:
        total_comp_value = computer_hit(total_comp_value)
    else:
        card_shower(comp_cards, 4)
    return total_comp_value
    
    
def winner_loser(money):
    global play_again
    if money <= 0:
        print("\n\nYou have lost all your winnings, we are kicking you out the Ahmecc Casino now")
        play_again = False
    else:
        choice = input("\n\nWould you like to go again? [y] or [n]:")
        if choice == "n":
            print(f"\n    Thank you for playing! You leave with {money}\n\n")
            print("""  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$  /$$     /$$ /$$$$$$$$
 /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$| $$__  $$|  $$   /$$/| $$_____/
| $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$ \  $$ /$$/ | $$      
| $$ /$$$$| $$  | $$| $$  | $$| $$  | $$| $$$$$$$   \  $$$$/  | $$$$$   
| $$|_  $$| $$  | $$| $$  | $$| $$  | $$| $$__  $$   \  $$/   | $$__/   
| $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$  \ $$    | $$    | $$      
|  $$$$$$/|  $$$$$$/|  $$$$$$/| $$$$$$$/| $$$$$$$/    | $$    | $$$$$$$$
 \______/  \______/  \______/ |_______/ |_______/     |__/    |________/""")
            play_again = False
    return play_again
DECK = [
    {"value": 10,
     "art": ''' 
 -------
|K      |
|       |
|       |
|       |
|      K|
 ------- '''},
    {"value": 10,
     "art": '''
 -------
|Q      |
|       |
|       |
|       |
|      Q|
 ------- '''},
    {"value": 10,
     "art": ''' 
 -------
|J      |
|       |
|       |
|       |
|      J|
 ------- '''},
    {"value": 10,
     "art": '''
 -------
|10     |
|       |
|       |
|       |
|     10|
 ------- '''},
    {"value": 9,
     "art": '''
 -------
|9      |
|       |
|       |
|       |
|      9|
 ------- '''},
    {"value": 8,
     "art": '''
 -------
|8      |
|       |
|       |
|       |
|      8|
 ------- '''},
    {"value": 7,
     "art": '''
 -------
|7      |
|       |
|       |
|       |
|      7|
 ------- '''},
    {"value": 6,
     "art": '''
 -------
|6      |
|       |
|       |
|       |
|      6|
 ------- '''},
    {"value": 5,
     "art": '''
 -------
|5      |
|       |
|       |
|       |
|      5|
 ------- '''},
    {"value": 4,
     "art": '''
 -------
|4      |
|       |
|       |
|       |
|      4|
 ------- '''},
    {"value": 3,
     "art": '''
 -------
|3      |
|       |
|       |
|       |
|      3|
 ------- '''},
    {"value": 2,
     "art": '''
 -------
|2      |
|       |
|       |
|       |
|      2|
 ------- '''},
    {"value": 11,
     "art": ''' 
-------
|A      |
|       |
|       |
|       |
|      A|
 ------- '''},

]
HIDDEN_CARD = '''
 -------
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
 ------- '''


play_again = True
while play_again:
    blackjack_logo() #This Block calls the Bet Function, and then stores the corresponding values
    bet_calculator_output = bet_calculator(money)
    money = bet_calculator_output[1]
    bet = bet_calculator_output[0]

    draw_repeat = True #repeats automatically in the event of a draw
    while draw_repeat:
        clear_page()
        user_cards = initial_card_selector(DECK)
        total_user_value = card_shower(user_cards, 1)[0] #Obtains INITIAL User Cards and then Print them Out
        time.sleep(0.5)
        comp_cards = initial_card_selector(DECK) #their inital deck
        total_comp_value = card_shower(comp_cards, 2)[0] #Obtains INITIAL Computer Cards and Prints them Out
        time.sleep(0.5)

        choose = input("\nWould you like another Hit [y] or are you Standing[n]: ") #lets them Hit
        if choose.upper() == "Y":
            while True:
                kreate = card_shower(extra_card_selector(user_cards, DECK), 1) #Gives New Card, works out New Total and Prints out their New Cards
                values = kreate[1] #List of values stored here
                total_user_value = kreate[0] #New Total user value stored here
                choose = input("\nWould you like another Hit [y] or are you Standing[n]: ") #Allows for them to choose another Hit
                if choose.upper() == "N":
                    break
        total_comp_value = end_output(total_comp_value)
        if total_user_value > 21:
            draw_repeat = False
            print(f"\n\nUnlucky You Went Bust. Computer Wins!")
            play_again = winner_loser(money)
        elif total_comp_value > 21:
            draw_repeat = False
            print(f"\n\nThe Computer went Bust. You Win!")
            play_again = winner_loser(money)
        elif total_user_value > total_comp_value:
            draw_repeat = False
            print(f"\n\nCongratulations You Win {bet * 2}, Your total of {total_user_value} was closer to 21 than the Computer!")
            money += bet * 2
            play_again = winner_loser(money)
        elif total_user_value < total_comp_value:
            draw_repeat = False
            print(f"\n\nUnlucky You Lost, The Computers total of {total_comp_value} was closer to 21 than You!")
            play_again = winner_loser(money)
        else:
            print(f"Its a Draw, You Both had a Value of {total_user_value}. We go Again")
            time.sleep(1)

