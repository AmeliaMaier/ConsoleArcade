'''
menu of game options with session history
-hangman
-guess my number
-connect 4
-...
'''

def print_main_menu(main_menu_dict):
    print('************************************************')
    print('**************** Console Arcade ****************')
    print('************************************************')
    for menu_option in main_menu_dict:
        print(f'{menu_option}: {main_menu_dict[menu_option]}')
def clear_history(game_history):
    game_history = []
def session_history(game_history):
    for record in game_history:
        print(record)
    user_input = input('Would you like to clear the history? (Y/N)')
    if user_input == 'Y':
        clear_history(game_history)


main_menu_dict = {'1':'Hangman', '2':'Guess My Number', '3':'TicTacToe', 'H':'Session History', 'Q':'Quit'}
menu_to_method_dict = {'1':'game = Hangman()', '2':'game = GuessMyNumber()', '3':'game = TicTacToe()', 'H':'Session History', 'Q':'Quit'}
game_history = []
while (True):
    user_input = ''
    print_main_menu(main_menu_dict)
    while not (user_input.strip() in main_menu_dict):
        user_input = input('Enter the numer for the game you would like to play. ')
    if user_input.strip() == 'Q':
        break
    if user_input.strip() == 'H':
        session_history(game_history)
        continue
    exec(menu_to_method_dict[user_input.strip()])
    game.run_game()
    game_history.append(game)
