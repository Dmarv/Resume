############################################################
# CIS 521: Homework 2
############################################################
import cProfile
import random
from copy import copy
from math import floor, factorial

student_name = "Daniel Marvin"


############################################################
# Imports
############################################################

# Include your imports here, if any are used.


############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    p = pow(n, 2)
    p_current = p
    d = n
    d_current = d
    for i in range(n - 1):
        p_current -= 1
        d_current -= 1
        p = p_current * p
        d = d_current * d
    return p / d
    pass


def num_placements_one_per_row(n):
    return pow(n, n)
    pass


def n_queens_valid(board):
    if len(board) < 2:
        return True
    li = []
    for i in range(len(board) - 1):
        if board[i] not in li:
            for j in range(len(board) - i - 1):
                if abs(board[i] - board[i + j + 1]) != j + 1:
                    li.append(board[i])
                else:
                    return False
        else:
            return False
    if board[-1] in li:
        return False
    return True

    pass

#checks if the next move is valid
def n_queens_valid_next(n, board):
    b = board[:]
    b.append(n)
    if n_queens_valid(b):
        return True
    return False
    pass

# finds all next valid moves and solves the problem recursively.
def n_queens_recur_(current_sol, n):
    solutions = []
    c = current_sol[:]
    possible_next = [i for i in range(n) if n_queens_valid_next(i, current_sol)]

    if len(possible_next) < 1:
        if len(c) == n:
            if n_queens_valid(c):
                solutions = current_sol[:]
        return solutions

    for i in range(len(possible_next)):
        c = current_sol[:]
        c.append(possible_next[i])
        r = n_queens_recur_(c, n)
        if len(r) > 0:
            for j in r:
                solutions.append(j)
    return solutions


def n_queens_solutions(n):
    li = []
    rtn = []

    current_sol = []
    solutions = n_queens_recur_(current_sol, n)
    li = solutions[:]
    temp = []
    for i in range(len(li)):
        if i % n == 0:
            rtn.append(temp)
            temp = []
        temp.append(li[i])
    rtn.append(temp)
    if len(rtn) > 0:
        del rtn[0]
    return rtn
    pass


# print(n_queens_solutions(11))


# x = [4, 2, 0, 5, 3, 1]
# print(n_queens_valid(x))


############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        self.board = board
        row = 0
        col = 0
        for i in board:
            row += 1
        for j in board[0]:
            col += 1
        self.row = row
        self.col = col
        pass

    # def __cmp__(self, other):
    #     for i in range(sel)

    def get_board(self):
        return self.board
        pass

    def perform_move(self, row, col):
        self.board[row][col] = not self.board[row][col]
        if row + 1 < self.row:
            self.board[row + 1][col] = not self.board[row + 1][col]
        if col + 1 < self.col:
            self.board[row][col + 1] = not self.board[row][col + 1]
        if row - 1 > -1:
            self.board[row - 1][col] = not self.board[row - 1][col]
        if col - 1 > -1:
            self.board[row][col - 1] = not self.board[row][col - 1]
        pass

    def scramble(self):
        for i in range(self.row):
            for j in range(self.col):
                if random.random() < 0.5:
                    self.perform_move(i, j)
        return self
        pass

    def is_solved(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j]:
                    return False
        return True
        pass

    def copy(self):
        li = []
        for i in range(self.row):
            li.append([self.board[i][j] for j in range(self.col)])
        p = LightsOutPuzzle(li)
        return p
        pass

    def successors(self):
        for i in range(self.row):
            for j in range(self.col):
                p = self.copy()
                p.perform_move(i, j)
                yield (i, j), p
        pass

    def find_solution(self):
        li_next = []
        li_visited = []
        solution = None
        li_solution = []
        for l, m in self.successors():
            li_next.append([l, m])
        while len(li_next) > 0:
            if li_next[0][1].is_solved():
                solution = li_next[0]
                break
            else:
                check = 0
                for i in li_visited:
                    if li_next[0][1].get_board() == i[1].get_board():
                        check = 1
                        break
                if check == 0:
                    for j, k in li_next[0][1].successors():
                        li_next.append([j, k])
                li_visited.append(li_next[0])
                del li_next[0]
        if solution == None:
            return None
        next_node = solution
        check = 0
        while True:
            li_solution.append(next_node[0])
            row = next_node[0][0]
            col = next_node[0][1]
            next_node[1].perform_move(row, col)
            if next_node[1].get_board() == self.get_board():
                break
            for n in li_visited:
                if n[1].get_board() == next_node[1].get_board():
                    next_node = n.copy()
                    break
        if li_solution == [(0, 0), (0, 0)]:
            del li_solution[0]
            del li_solution[0]
        return li_solution[::-1]
        pass


def create_puzzle(rows, cols):
    li = []
    for i in range(rows):
        li.append([False for j in range(cols)])
    return LightsOutPuzzle(li)
    pass


def pretty_print(board):
    for i in board:
        print("%s\n" % i)


############################################################
# Section 3: Linear Disk Movement
############################################################

class LinearDiskMovement(object):

    def __init__(self, grid):
        self.grid = grid
        self.length = len(grid)
        n = 0
        for i in grid:
            if i != 0:
                n += 1
        self.disks = n
        pass

    def get_grid(self):
        return self.copy_grid().grid

    def move_disk(self, start, end):
        self.grid[end] = self.grid[start]
        self.grid[start] = 0

    def move_is_valid(self, start, end):
        if start == end:
            return False
        if self.grid[end] != 0:
            return False
        if self.grid[start] == 0:
            return False
        if abs(end - start) > 2:
            return False
        if abs(end - start) == 1:
            return True
        if abs(end - start) == 2:
            if end > start:
                if self.grid[start + 1] == 0:
                    return False
            else:
                if self.grid[start - 1] == 0:
                    return False
        return True

    def copy_grid(self):
        cop = self.grid[:]
        cop_ob = LinearDiskMovement(cop)
        return cop_ob

    def next_valid_moves(self):
        for i in range(self.length):
            for j in range(self.length):
                if self.move_is_valid(i, j):
                    new_ob = self.copy_grid()
                    new_ob.move_disk(i, j)
                    yield (i, j), new_ob

    def ldm_iden_solved(self):
        for i in range(self.disks):
            if self.grid[- (i + 1)] != 1:
                return False
        return True

    def ldm_dist_solved(self):
        for i in range(self.disks):
            if self.grid[- (i + 1)] != i + 1:
                return False
        return True

    def ldm_iden_initial_state(self):
        for i in range(self.disks):
            if self.grid[i] != 1:
                return False
        return True

    def ldm_dist_initial_state(self):
        for i in range(self.disks):
            if self.grid[i] != i + 1:
                return False
        return True


def make_new_iden_grid(length, disks):
    grid = [0] * length
    for i in range(disks):
        grid[i] = 1
    return grid


def make_new_dist_grid(length, disks):
    grid = [0] * length
    for i in range(disks):
        grid[i] = i + 1
    return grid


def solve_identical_disks(length, n):
    if length == n:
        return []
    li_visited = []
    li_next = []
    solution = 0
    g = make_new_iden_grid(length, n)
    start_grid = LinearDiskMovement(g)

    for move in start_grid.next_valid_moves():
        li_next.append(move)
    while len(li_next) > 0:
        current_obj = li_next[0]
        if current_obj[1].ldm_iden_solved():
            solution = current_obj
            break
        else:
            visit = 0
            for visited in li_visited:
                if visited[1].get_grid() == current_obj[1].get_grid():
                    visit = 1
                    break
            if visit == 0:
                for move1 in current_obj[1].next_valid_moves():
                    li_next.append(move1)
                li_visited.append(li_next[0])
            del li_next[0]
    li_solution = []
    current_move = solution
    while True:
        li_solution.append(current_move[0])
        if current_move[1].ldm_iden_initial_state():
            break
        start_current = current_move[0][1]
        end_current = current_move[0][0]
        current_move[1].move_disk(start_current, end_current)
        for i in li_visited:
            if i[1].get_grid() == current_move[1].get_grid():
                current_move = i
                break
    rtn = li_solution[::-1]
    del rtn[0]
    return rtn
    pass


def solve_distinct_disks(length, n):
    if length == n:
        return []
    li_visited = []
    li_next = []
    solution = 0
    g = make_new_dist_grid(length, n)
    start_grid = LinearDiskMovement(g)

    for move in start_grid.next_valid_moves():
        li_next.append(move)
    while len(li_next) > 0:
        current_obj = li_next[0]
        if current_obj[1].ldm_dist_solved():
            solution = current_obj
            break
        else:
            visit = 0
            for visited in li_visited:
                if visited[1].get_grid() == current_obj[1].get_grid():
                    visit = 1
                    break
            if visit == 0:
                for move1 in current_obj[1].next_valid_moves():
                    li_next.append(move1)
                li_visited.append(li_next[0])
            del li_next[0]
    li_solution = []
    current_move = solution
    while True:
        li_solution.append(current_move[0])
        if current_move[1].ldm_dist_initial_state():
            break
        start_current = current_move[0][1]
        end_current = current_move[0][0]
        current_move[1].move_disk(start_current, end_current)
        for i in li_visited:
            if i[1].get_grid() == current_move[1].get_grid():
                current_move = i
                break
    rtn = li_solution[::-1]
    del rtn[0]
    return rtn
    pass


# p = make_new_iden_grid(4, 2)
#
# q = solve_identical_disks(5, 3)
# r = solve_distinct_disks(5, 3)
# print(r)


# pr = cProfile.Profile()
# pr.enable()
# print(solve_distinct_disks(7, 4))
# pr.disable()
#
# pr.print_stats(sort="calls")


