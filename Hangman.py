import random

class Hangman():
    def __init__(self):
        self.ran_word = random.choice(['these','are', 'just','seed', 'values'])
        self.lives = 5
        self.win = False
        self.answer = ['_']*len(self.ran_word)
        self.guesses = ['Empty']

    def print_lives_and_word(self):
        print("Lives:" + "*"*self.lives + "_"*(self.max_life - self.lives))
        guesses_str = ''.join(char for char in sorted(self.guesses))
        print("Guesses: " + guesses_str)
        answer_str = ''.join(char for char in self.answer)
        print(answer_str)

    def check_guess(self, guess):
        if 'Empty' in self.guesses:
            self.guesses = []
        if guess in self.guesses:
            print("You already guessed that letter, try again.")
            return
        self.guesses.append(guess)
        if guess in self.ran_word:
            for ind, char in enumerate(self.ran_word):
                if guess == char:
                    self.answer[ind] = guess
            if list(self.ran_word) == self.answer:
                self.win = True
                print("Congradulations. You won.")
            return
        self.lives -= 1
        print("No, that letter is not in the word.")

    def run_game(self):
        self.max_life = self.lives
        while not (self.win or self.lives == 0):
            user_input = ''
            self.print_lives_and_word()
            while not (user_input == '1' or (len(user_input.strip())==1 and not user_input.strip().isdigit())):
                user_input = input("Enter a letter to guess or 1 to Quit: ")
            if user_input == '1':
                return
            self.check_guess(user_input.strip().lower())

    def __str__(self):
        if self.win:
            result = 'Win'
        else:
            result = 'Loss'
        return f'Hangman: {result}'
