############################################################
# CIS 521: Homework 3a
############################################################
import queue
import sys

import numpy as np

student_name = "Type your full name here."

############################################################
# Imports
############################################################

# Include your imports here, if any are used.

import collections
import copy
import itertools
import random
import math


############################################################
# Section 1: Dominoes Game
############################################################

# make a Domino board object
def create_dominoes_game(rows, cols):
    board = []
    for i in range(rows):
        board.append([False for j in range(cols)])
    game = DominoesGame(board)
    return game
    pass


class DominoesGame(object):

    # Required
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        try:
            self.cols = len(board[0])
        except IndexError:
            self.cols = 0
        self.limit = 0
        self.leaf = 0
        self.depth = 0
        self.player = None

        pass

    def get_board(self):
        return self.board
        pass

    # resets board by setting every location to False
    def reset(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.board[i][j] = False
        pass

    def is_legal_move(self, row, col, vertical):

        # if peice on board in this location, no legal move
        if self.board[row][col]:
            return

        # if at the edge or adjacent location is filled, no legal move
        if vertical:
            if row == self.rows - 1 or self.board[row + 1][col]:
                return False
        if not vertical:
            if col == self.cols - 1 or self.board[row][col + 1]:
                return False

        return True
        pass

    def legal_moves(self, vertical):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.is_legal_move(i, j, vertical):
                    yield i, j
        pass

    def perform_move(self, row, col, vertical):
        # set the position of row/col to True and the appropriate adjacent space
        self.board[row][col] = True
        if vertical:
            self.board[row + 1][col] = True
        if not vertical:
            self.board[row][col + 1] = True
        self.depth += 1
        pass

    def game_over(self, vertical):
        # if there are no valid legal moves left for this place, the game ends
        if len(list(self.legal_moves(vertical))) == 0:
            return True
        return False
        pass

    def copy(self):
        x = DominoesGame(copy.deepcopy(self.get_board()))
        x.limit = self.limit + 0
        x.leaf = copy.deepcopy(self.leaf)
        x.depth = self.depth + 0
        x.player = self.player
        return x
        pass

    def successors(self, vertical):
        for i, j in self.legal_moves(vertical):
            cop = self.copy()
            cop.perform_move(i, j, vertical)
            yield (i, j), cop

        pass

    def get_random_move(self, vertical):
        x = list(self.legal_moves(vertical))
        return random.choice(x)
        pass

    def number_of_next_moves(self, vertical):
        return len(list(self.legal_moves(vertical)))

    def board_eval(self, vertical):

        current_player = self.number_of_next_moves(vertical)
        other_player = self.number_of_next_moves(not vertical)
        # pretty_print(self.get_board())
        # print(current_player - other_player)
        return current_player - other_player

    def max_value(self, state, alpha, beta):
        counter = 0
        local_max = -math.inf
        for i, j in self.successors(state):
            temp, number = j.value(not state, alpha, beta)
            counter += number
            local_max = max(local_max, temp)
            alpha = max(alpha, local_max)
            if beta <= alpha:
                break
        return local_max, counter

    def min_value(self, state, alpha, beta):
        counter = 0
        local_min = math.inf
        for i, j in self.successors(state):
            temp, number = j.value(not state, alpha, beta)
            counter += number
            local_min = min(local_min, temp)
            beta = min(beta, local_min)
            if beta <= alpha:
                break
        return local_min, counter

    def value(self, state, alpha, beta):

        if self.depth == self.limit or self.game_over(state):
            return self.board_eval(self.player), 1

        if self.depth % 2 == 0:
            return self.max_value(state, alpha, beta)

        if self.depth % 2 == 1:
            return self.min_value(state, alpha, beta)

    def get_best_move(self, vertical, limit):
        self.limit = limit
        self.player = vertical
        self.depth = 0
        li = []
        counter = 0
        alpha = -math.inf
        beta = math.inf
        for i, j in self.successors(vertical):
            temp, number = j.value(not vertical, alpha, beta)
            counter += number
            alpha = max(alpha, temp)
            li.append((i, temp))
        rtn = (0, -math.inf)
        for i in li:
            if i[1] > rtn[1]:
                rtn = i
        x = 0
        y = 0
        x = rtn[0]
        y = rtn[1]
        r = (x, y, counter)
        return r


def pretty_print(board):
    for i in board:
        print(i)


# b = [[False] * 3 for i in range(3)]
# g = DominoesGame(b)
# g.perform_move(0, 1, True)
# print(g.get_best_move(False, 2))

# b = [[False] * 3 for i in range(3)]
# g = DominoesGame(b)
# print(g.get_best_move(True, 2))

