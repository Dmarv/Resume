import cProfile
import queue

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
# Sudoku Solver
############################################################

def sudoku_cells():
    li = []
    for i in range(9):
        for j in range(9):
            li.append((i, j))
    return li
    pass


def sudoku_arcs():
    li = []
    for i in sudoku_cells():
        boxi0 = math.floor(i[0] / 3)
        boxi1 = math.floor(i[1] / 3)
        for j in sudoku_cells():
            if not i == j:
                boxj0 = math.floor(j[0] / 3)
                boxj1 = math.floor(j[1] / 3)
                if i[0] == j[0] or i[1] == j[1] or (boxi0 == boxj0 and boxi1 == boxj1):
                    li.append((i, j))
    return li
    pass


def read_board(path):
    diction = {}
    file = open(path, 'r')
    Lines = file.readlines()
    line_counter = 0
    valid = '123456789'
    for line in Lines:
        letter_counter = 0
        for letter in line:
            if letter == '*':
                diction[line_counter, letter_counter] = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
            if letter in valid:
                diction[line_counter, letter_counter] = set([int(letter)])
            letter_counter += 1
        line_counter += 1
    return diction
    pass


def neighbours():
    diction = {}
    for i in sudoku_cells():
        li = []
        for j in sudoku_cells():
            if (i, j) in sudoku_arcs():
                li.append(j)
        diction[i] = li
    return diction


class Sudoku(object):
    CELLS = sudoku_cells()
    ARCS = sudoku_arcs()
    NEIGHBOURS = neighbours()

    def __init__(self, board):
        self.board = board
        pass

    def get_values(self, cell):
        return self.board[cell[0], cell[1]]
        pass

    def copy_sudoku(self):
        return Sudoku(copy.deepcopy(self.board))

    def get_neighbours(self, cell):
        return Sudoku.NEIGHBOURS[cell[0], cell[1]]

    def get_box_neighbours(self, cell):
        li = []
        i = math.floor(cell[0] / 3)
        j = math.floor(cell[1] / 3)
        for k in self.get_neighbours(cell):
            if math.floor(k[0] / 3) == i and math.floor(k[1] / 3) == j:
                li.append(k)
        return li

    def get_next_unsolved(self):
        for i in Sudoku.CELLS:
            if len(self.get_values(i)) > 1:
                return i

    def remove_inconsistent_values(self, cell1, cell2):
        boo = (cell1, cell2) in Sudoku.ARCS
        temp1 = self.get_values(cell1)
        temp2 = self.get_values(cell2)
        if not boo or len(temp2) > 1 or len(temp1) == 1:
            return False
        new = []
        for i in temp1:
            if not i in temp2:
                new.append(i)
        self.board[cell1[0], cell1[1]] = set(new)
        return True
        pass

    def check_box(self, cell):
        li = self.get_box_neighbours(cell)
        for i in self.get_values(cell):
            test = False
            for j in li:
                if i in self.get_values(j):
                    test = True
                    break
            if not test:
                self.board[cell[0], cell[1]] = set([i])
                return True
        return False

    def solved(self):
        for i in Sudoku.CELLS:
            if len(self.get_values(i)) > 1:
                return False
            for j in self.get_neighbours(i):
                if len(self.get_values(j)) > 1:
                    return False
                if self.get_values(j) == self.get_values(i):
                    return False
        return True

    def solvable(self):
        for i, j in Sudoku.ARCS:
            if len(self.get_values(i)) == 1 and len(self.get_values(j)) == 1:
                if self.get_values(i) == self.get_values(j):
                    return False
        return True

    def pretty_print(self):
        for i in range(9):
            li = []
            for j in range(9):
                temp = self.board[i, j]
                if len(temp) > 1:
                    li.append('*')
                else:
                    li.append(temp)
            print(li)

    def infer_ac3(self):
        limit = 0
        counter = 0
        pre = 0
        while not self.solved():
            if self.solved():
                break
            counter = 0
            for i in Sudoku.CELLS:
                for j in Sudoku.CELLS:
                    if self.remove_inconsistent_values(i, j):
                        counter += 1
            if pre == counter:
                limit += 1
            if limit > 1:
                break
            pre = counter
        pass

    def infer_improved(self):
        while not self.solved():
            self.infer_ac3()
            if self.solved():
                break
            for i in Sudoku.CELLS:
                if not len(self.get_values(i)) == 1:
                    self.check_box(i)
        pass

    def infer_improved_w_rtn(self):
        counter = 0
        total = 0
        while not self.solved():
            self.infer_ac3()
            if self.solved():
                break
            for i in Sudoku.CELLS:
                if not len(self.get_values(i)) == 1:
                    if self.check_box(i):
                        counter += 1
            # print(counter)
            if total == counter:
                return False
            total = counter
        return True
        pass

    def recur(self):
        rtn = False, -1

        while not self.solved():
            solvable = self.solvable()
            if not solvable:
                return False, -1
            solved = self.infer_improved_w_rtn()
            if not solved:
                nex = self.get_next_unsolved()
                if nex is None:
                    return False, -1
                li = self.get_values(nex)
                counter = 1
                maxi = len(li)
                for guess in li:
                    # print("counter", counter, " maxi", maxi)
                    counter += 1
                    # print("guess", guess)
                    p = self.copy_sudoku()
                    p.board[nex[0], nex[1]] = {guess}
                    rtn = p.recur()
                    if rtn[0]:
                        r = [guess]
                        if not rtn[1] == -1:
                            for i in rtn[1]:
                                r.append(i)
                        return True, r
                if counter >= maxi:
                    return False, -1

                        # break
        #         if rtn[0]:
        #             break
        #
        return True, rtn[1]

    def infer_with_guessing(self):
        rtn = self.infer_improved_w_rtn()
        self.pretty_print()
        while not self.solved():
            # print("in guess")
            cell = self.get_next_unsolved()
            rtn = self.recur()
            if rtn[0]:
                for i in rtn[1]:
                    self.board[cell[0], cell[1]] = {i}
                    self.infer_improved_w_rtn()
                    cell = self.get_next_unsolved()

        pass


pr = cProfile.Profile()
pr.enable()

sudoku = Sudoku(read_board('sudoku/cust.txt'))
sudoku.pretty_print()
print(sudoku.infer_with_guessing())
sudoku.pretty_print()

pr.disable()
pr.print_stats(sort="calls")


############################################################
# Feedback
############################################################

# Just an approximation is fine.
feedback_question_1 = 10

feedback_question_2 = """
The back tracking in part 7 was difficult, but not as hard as mini-max.
"""

feedback_question_3 = """
No, this assignment appropriately tested our knowledge of ac3 and was fun to work on. 
"""
