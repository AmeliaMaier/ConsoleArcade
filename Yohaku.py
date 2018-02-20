'''each puzzle is either additive or multiplicative. fill in the empty squares such that they
give the sum/product shown in each row and column.
----------
| 1 2 | 3
| 3 4 | 7
---------
| 4 6 | +
----------
'''

import numpy as np
import random as ran

class Yohaku():
    def __init__(self):
        self.win = False
        self.answer_array = np.random.randint(1,100,4).reshape(2,2)
        self.operator = '+' if ran.randint(0,1) == 0 else '*'# 0 = +; 1 = *
        self.board = np.zeros(9).reshape(3,3)

    def create_board(self):
        if np.array_equal(self.board, np.zeros(9).reshape(3,3)):
            self.board[0:2, 0:2] = np.array([[0,0],[0,0]])
            if self.operator == '+':
                self.board[2,2] = 0
                self.board[0:2,2:3] = self.answer_array.sum(axis=1).reshape(2,1)
                self.board[2:3,0:2] = self.answer_array.sum(axis=0).reshape(1,2)
            elif self.operator == '*':
                self.board[2,2] = 1
                self.board[0:2,2:3] = self.answer_array.prod(axis=1).reshape(2,1)
                self.board[2:3,0:2] = self.answer_array.prod(axis=0).reshape(1,2)
            else:
                print("Please see IT, the oporator is not recognized")
        else:
            self.board[self.x_coordinate-1, self.y_coordinate-1] = self.guess_value

    def print_board(self):
        board_output = "__________________\n"
        for r_ind, row in enumerate(self.board):
            for c_ind, value in enumerate(row):
                if r_ind == 2 and c_ind == 2:
                    board_output += f" {self.operator} "
                    continue
                board_output += f"{self.board[r_ind,c_ind]} |"
            board_output += "\n__________________\n"
        print (board_output)

    def check_guess(self):
        split_user_input = self.user_input.split(" ")
        if not len(split_user_input) == 2:
            return False
        if not split_user_input[1].strip().isdigit():
            return False
        self.guess_value = int(split_user_input[1].strip())
        split_coordinates = split_user_input[0].split(",")
        if not len(split_coordinates) == 2:
            return False
        if not (split_coordinates[0].strip().isdigit() and split_coordinates[1].strip().isdigit()):
            return False
        self.x_coordinate = int(split_coordinates[0].strip())
        self.y_coordinate = int(split_coordinates[1].strip())
        if not ((self.x_coordinate == 0 or self.x_coordinate == 1) and (self.y_coordinate == 0 or self.y_coordinate == 1)):
            return False
        return True

    def check_win(self):
        if self.operator == '+':
            if self.board[0,0]+self.board[0,1] == self.board[0,2] and self.board[1,0]+self.board[1,1] == self.board[1,2]:
                if self.board[0,0]+self.board[1,0] == self.board[2,0] and self.board[0,1]+self.board[1,1] == self.board[2,1]:
                    return True
        elif self.operator == '*':
            if self.board[0,0]*self.board[0,1] == self.board[0,2] and self.board[1,0]*self.board[1,1] == self.board[1,2]:
                if self.board[0,0]*self.board[1,0] == self.board[2,0] and self.board[0,1]*self.board[1,1] == self.board[2,1]:
                    return True
        else:
            print("Please see IT, the oporator is not recognized")
        return False

    def run_game(self):
        self.create_board()
        self.turn = 1
        while not self.win:
            self.print_board()
            self.user_input = ''
            required_inputs = False
            while self.user_input == '' and not required_inputs:
                self.user_input = input("Enter the cordinates of the value you would like to enter and the value you would like to set or q to quit. ex. 1,1 23: ")
                if self.user_input == 'q':
                    return
                required_input = self.check_guess()
            self.create_board()
            if self.turn >= 4:
                self.win = self.check_win()
            self.turn += 1
            if self.win:
                print("Congradulations. That is correct!")
