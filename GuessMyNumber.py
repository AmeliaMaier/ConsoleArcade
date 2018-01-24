import random

class GuessMyNumber():
    def __init__(self):
        self.ran_num = random.randint(1, 101)
        self.win = False
        self.turn = 0
        self.past_diff = 0

    def check_answer(self):
        current_diff = abs(self.ran_num - int(self.user_input.strip()))
        if current_diff == 0:
            print('That is correct. You must be psychic.')
            self.win = True
            return
        if self.turn == 1:
            if current_diff <= 10:
                print('So close. You are hot.')
                self.past_diff = current_diff
                return
            print('Try again; you are cold.')
            self.past_diff = current_diff
            return
        if self.past_diff >= current_diff:
            print('Getting warmer')
            self.past_diff = current_diff
            return
        if self.past_diff == current_diff:
            print('No change')
            self.past_diff = current_diff
            return
        print('You are getting colder.')
        self.past_diff = current_diff

    def run_game(self):
        self.user_input = ''
        self.turn = 1
        while self.user_input == '' and not self.user_input.strip().isdigit():
            self.user_input = input('Try to guess my number: ')
        self.check_answer()
        while not self.win:
            self.user_input = ''
            self.turn += 1
            while not (self.user_input == 'Q' or self.user_input.strip().isdigit()):
                self.user_input = input('Try again or type Q to give up: ')
            if self.user_input == 'Q':
                return
            self.check_answer()
    def __str__(self):
        if self.win:
            result = 'Win'
        else:
            result = 'Loss'
        return f'Guess My Number: {result}'
