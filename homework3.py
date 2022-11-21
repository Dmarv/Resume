############################################################
# CIS 521: Homework 3
############################################################
import math

student_name = "Daniel Marvin"

############################################################
# Imports
############################################################

import random
from copy import deepcopy
import cProfile
import queue


############################################################
# Section 1: Tile Puzzle
############################################################

def create_tile_puzzle(rows, cols):
    li = []
    n = 1
    for i in range(rows):
        temp = []
        for j in range(cols):
            temp.append(n)
            n += 1
        li.append(temp)
    li[rows - 1][cols - 1] = 0
    return li

    pass


class TilePuzzle(object):

    # Required
    def __init__(self, board):
        self.board = board
        r = 0
        c = 0
        z = 0
        for i in board:
            r += 1
        self.rows = r
        for j in board[0]:
            c += 1
        self.cols = c
        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] == 0:
                    z = (i, j)
                    break
        self.zero = z
        self.depth = 0
        self.moves = []
        pass

    def __lt__(self, other):
        if self.depth < other.depth:
            return True
        return False

    def get_board(self):
        return self.board
        pass

    def perform_move(self, direction):
        zero_row = self.zero[0]
        zero_col = self.zero[1]
        temp = 0
        if direction == 'down':
            if zero_row == self.rows - 1:
                return False
            temp = self.board[zero_row + 1][zero_col]
            self.board[zero_row + 1][zero_col] = 0
            self.board[zero_row][zero_col] = temp
            self.zero = (zero_row + 1, zero_col)
            self.depth += 1
            self.moves.append('down')
            return True
        if direction == 'up':
            if zero_row == 0:
                return False
            temp = self.board[zero_row - 1][zero_col]
            self.board[zero_row - 1][zero_col] = 0
            self.board[zero_row][zero_col] = temp
            self.zero = (zero_row - 1, zero_col)
            self.depth += 1
            self.moves.append('up')
            return True
        if direction == 'right':
            if zero_col == self.cols - 1:
                return False
            temp = self.board[zero_row][zero_col + 1]
            self.board[zero_row][zero_col + 1] = 0
            self.board[zero_row][zero_col] = temp
            self.zero = (zero_row, zero_col + 1)
            self.depth += 1
            self.moves.append('right')
            return True
        if direction == 'left':
            if zero_col == 0:
                return False
            temp = self.board[zero_row][zero_col - 1]
            self.board[zero_row][zero_col - 1] = 0
            self.board[zero_row][zero_col] = temp
            self.zero = (zero_row, zero_col - 1)
            self.depth += 1
            self.moves.append('left')
            return True
        pass

    def scramble(self, num_moves):
        for i in range(num_moves):
            self.perform_move(random.choice(['up', 'down', 'right', 'left']))
        pass

    def is_solved(self):
        n = 1
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != n:
                    return False
                if i == self.rows - 1:
                    if j == self.cols - 2:
                        n = -1
                n += 1
        return True
        pass

    def copy(self):
        b = []
        for i in range(self.rows):
            c = []
            for j in range(self.cols):
                c.append(self.board[i][j])
            b.append(c)
        p = TilePuzzle(b)
        p.depth = deepcopy(self.depth)
        d = []
        for i in self.moves:
            d.append(i)
        p.moves = d
        return p
        pass

    def successors(self):

        for i in ['up', 'down', 'left', 'right']:
            p = self.copy()
            if p.perform_move(i):
                yield (i, p)
        pass

    # Required
    def find_solutions_iddfs(self):
        if self.rows == 1:
            return []
        if self.cols == 1:
            return []
        limit = 0
        li_visited = []
        li_solutions = []
        li_next = []
        ex = 0
        self.depth = 0
        self.moves = []
        if self.is_solved():
            return []
        for i in self.successors():
            li_next.append(i)

        while True:
            for i in li_next:
                if i[1].depth == limit:
                    if i[1].is_solved():
                        yield i[1].moves
                        ex = 1
                    for j in i[1].successors():
                        li_next.append(j)
            if ex == 1:
                return []
            for k in li_next:
                if k[1].depth == limit:
                    li_visited.append(k)
                    li_next.remove(k)
            limit += 1
        pass

    def manhatten_distance(self, correct_position, correct_loc_dict):
        sum_dist = 0
        p = correct_position
        correct_location = correct_loc_dict
        current_location = {}
        for i in range(self.rows):
            for j in range(self.cols):
                current_location[self.board[i][j]] = (i, j)
        for i in range(self.rows * self.cols):
            if not i == 0:
                curl = current_location.get(i)
                corl = correct_location.get(i)
                x = abs(curl[0] - corl[0])
                y = abs(curl[1] - corl[1])
                sum_dist = sum_dist + x + y
        return sum_dist

    def make_libary(self):
        correct_location = {}
        n = 1
        for i in range(self.rows):
            for j in range(self.cols):
                correct_location[n] = (i, j)
                if i == self.rows - 1:
                    if j == self.cols - 2:
                        n = -1
                n += 1
        return correct_location

    # Required
    def find_solution_a_star(self):
        li_next = queue.PriorityQueue()
        li_solution = []
        li_visited = []
        self.depth = 0
        self.moves = []
        correct_position = TilePuzzle(create_tile_puzzle(self.rows, self.cols))
        correct_loc_dict = self.make_libary()
        if self.is_solved():
            return []
        for i in self.successors():
            value = i[1].depth + i[1].manhatten_distance(correct_position, correct_loc_dict)
            li_next.put((value, i[1]))

        count = 50
        while not li_next.empty():
            if len(li_solution) > 0:
                count -= 1
            if count == 0:
                break
            ex = 0
            temp = li_next.get()
            for j in li_visited:
                if temp[1].board == j[1].board:
                    ex = 1
            if ex == 0:
                if temp[1].is_solved():
                    li_solution.append(temp[1].moves)
                li_visited.append(temp)
                for i in temp[1].successors():
                    v = temp[1].depth + temp[1].manhatten_distance(correct_position, correct_loc_dict)
                    li_next.put((v, i[1]))
        shortest = li_solution[0]
        if len(li_solution) > 1:
            for i in li_solution:
                if len(i) < len(shortest):
                    shortest = i
        return shortest

        pass

    def pretty_print(self):
        for i in range(self.rows):
            print(self.board[i])

    def leng(self):
        i = 0
        for i in self.moves:
            i += 1
        return 1


def opposite(string):
    if string == 'up':
        return 'down'
    if string == 'down':
        return 'up'
    if string == 'right':
        return 'left'
    if string == 'left':
        return 'right'


# p = TilePuzzle(create_tile_puzzle(2, 2))
# p.scramble(50)
# p.pretty_print()
#
# print(p.find_solution_a_star())
# for i in p.find_solutions_iddfs():

#     print(i)

# pr = cProfile.Profile()
# pr.enable()
# p.find_solution_a_star()
# pr.disable()
#
# pr.print_stats(sort="calls")


############################################################
# Section 2: Grid Navigation
############################################################
class GridNavigation(object):

    def __init__(self, grid, start, goal):
        self.grid = grid
        n = 0
        m = 0
        for i in self.grid:
            n += 1
        for j in self.grid[0]:
            m += 1
        self.depth = 0
        self.rows = n
        self.cols = m
        self.move = 0
        self.sofa = 0
        self.start = start
        self.current_location = start
        self.goal = goal

    def __lt__(self, other):
        if self.sofa < other.sofa:
            return True
        return False

    def grid_nav_move(self, direction):
        a = ['up', 'down', 'left', 'right', 'up-left', 'up-right', 'down-left', 'down-right']
        if direction not in a:
            return False
        old_location = self.current_location
        row = 0
        col = 0
        if direction == 'up':
            row = -1
        if direction == 'down':
            row = 1
        if direction == 'left':
            col = -1
        if direction == 'right':
            col = 1
        if direction == 'up-left':
            row = -1
            col = -1
        if direction == 'up-right':
            row = -1
            col = 1
        if direction == 'down-left':
            row = 1
            col = -1
        if direction == 'down-right':
            row = 1
            col = 1
        new_location = (old_location[0] + row, old_location[1] + col)
        if new_location[0] < 0 or new_location[1] < 0 or new_location[0] > self.rows - 1 \
                or new_location[1] > self.cols - 1 \
                or self.grid[new_location[0]][new_location[1]] == True:
            return False
        self.current_location = new_location
        self.move = direction
        self.depth += 1
        if len(direction) > 5:
            self.sofa += 1.4142
        else:
            self.sofa += 1
        return True

    def copy_grid(self):
        p = GridNavigation(self.grid, self.start, self.goal)
        p.depth = self.depth + 0
        a = slice(self.depth + 1)
        # p.moves = self.moves[a]
        p.current_location = (self.current_location[0] + 0, self.current_location[1] + 0)
        p.sofa = self.sofa + 0
        return p

    def grid_successors(self):
        next_move = ['up', 'down', 'left', 'right', 'up-left', 'up-right', 'down-left', 'down-right']
        for i in next_move:
            p = self.copy_grid()
            if p.grid_nav_move(i):
                yield p

    def grid_huristic(self):

        x = abs(self.current_location[0] - self.goal[0])
        y = abs(self.current_location[1] - self.goal[1])
        z = min(x, y)
        a = max(x, y)
        b = a - z
        a = (math.sqrt(2) * z) + b

        c = abs(self.current_location[0] - self.start[0])
        d = abs(self.current_location[1] - self.start[1])
        e = min(c, d)
        f = max(c, d)
        g = f - e
        h = (math.sqrt(2) * e) + g
        return a + h + 10 * self.sofa

    def grid_solved(self):
        if self.current_location == self.goal:
            return True
        return False

    def print_nicely(self):
        for i in range(self.rows):
            print(self.grid[i])

    def translate(self, goal, li_visited):
        rtn = [goal]
        z = li_visited[goal[0]][goal[1]][1]
        counter = 1
        while not z == 0:
            op = oppos(z)
            row = 0
            col = 0
            prev = rtn[counter - 1]
            if op == 'up':
                row = -1
            if op == 'down':
                row = 1
            if op == 'left':
                col = -1
            if op == 'right':
                col = 1
            if op == 'up-left':
                row = -1
                col = -1
            if op == 'up-right':
                row = -1
                col = 1
            if op == 'down-left':
                row = 1
                col = -1
            if op == 'down-right':
                row = 1
                col = 1
            current = (prev[0] + row, prev[1] + col)
            rtn.append(current)
            counter += 1
            z = li_visited[current[0]][current[1]][1]
        return rtn[::-1]


def oppos(string):
    if string == 'up':
        return 'down'
    if string == 'down':
        return 'up'
    if string == 'left':
        return 'right'
    if string == 'right':
        return 'left'
    if string == 'up-left':
        return 'down-right'
    if string == 'up-right':
        return 'down-left'
    if string == 'down-left':
        return 'up-right'
    if string == 'down-right':
        return 'up-left'


def make_bool_grid(row, col):
    grid = []
    for i in range(row):
        grid.append([False for j in range(col)])
    return grid


def find_path(start, goal, scene):
    if start == goal:
        return []
    my_grid = GridNavigation(scene, start, goal)
    li_next = queue.PriorityQueue()
    li_visited = make_bool_grid(my_grid.rows, my_grid.cols)

    a = (my_grid.grid_huristic(), my_grid)
    li_next.put(a)

    while not li_next.empty():
        next_location = li_next.get()[1]
        x = next_location.current_location[0]
        y = next_location.current_location[1]
        if next_location.grid_solved():
            li_visited[x][y] = (next_location.sofa, next_location.move)
            return next_location.translate(goal, li_visited)
        li_visited[x][y] = (next_location.sofa, next_location.move)
        for i in next_location.grid_successors():
            z = i.current_location[0]
            a = i.current_location[1]
            if li_visited[z][a] == False:
                li_next.put((i.grid_huristic(), i))
                li_visited[z][a] = (i.sofa, i.move)
            else:
                if li_visited[z][a][0] > i.sofa:
                    li_visited[z][a] = (i.sofa, i.move)
                    li_next.put((i.grid_huristic(), i))
    return None
    pass


#makes a grid where true statments are walls and False is open space

# p = make_bool_grid(20, 20)
#
# for i in range(15):
#     p[i][3] = True
# for j in range(10):
#     p[15][j+3] = True
#
# q = GridNavigation(p, (0,0), (0,0))
# q.print_nicely()
#
# pr = cProfile.Profile()
# pr.enable()
# print(find_path((0, 2), (14, 4), p))
# pr.disable()
#
# pr.print_stats(sort="calls")


############################################################
# Section 3: Linear Disk Movement, Revisited
############################################################

class DistinctDisk:
    def __init__(self, board):
        self.board = board
        self.length = len(self.board)
        n = 0
        for i in self.board:
            if not i == -1:
                n += 1
        self.disks = n
        self.sofa = 0
        self.move = None

    def __lt__(self, other):
        if self.sofa < other.sofa:
            return True
        return False

    def get_board(self):
        return self.copy_grid().board

    def move_disk(self, start, end):
        self.board[end] = self.board[start]
        self.board[start] = -1
        self.sofa += 1
        # stored backwards since we'll need to traverse the li_visited to find the answer
        self.move = (end, start)

    def move_is_valid(self, start, end):
        if start == end:
            return False
        x = abs(end - start)
        if self.board[end] != -1:
            return False
        if self.board[start] == -1:
            return False
        if x > 2:
            return False
        if x == 1:
            return True
        if x == 2:
            if end > start:
                if self.board[start + 1] == -1:
                    return False
            else:
                if self.board[start - 1] == -1:
                    return False
        return True

    def copy_grid(self):
        cop = self.board[:]
        cop[0] += 0
        cop_ob = DistinctDisk(cop)
        cop_ob.sofa = self.sofa + 0
        return cop_ob

    def next_valid_moves(self):
        for i in range(self.length):
            for j in range(self.length):
                if self.move_is_valid(i, j):
                    new_ob = self.copy_grid()
                    new_ob.move_disk(i, j)
                    yield new_ob

    def dist_solved(self):
        for i in range(self.disks):
            if self.board[- (i + 1)] != i:
                return False
        return True

    def dist_initial_state(self):
        for i in range(self.disks):
            if self.board[i] != i:
                return False
        return True

    def disk_heuristic(self):
        sum = 0
        y = self.length
        # po = .5 + math.floor(y / (self.disks + 1))

        for i in range(self.disks):
            for j in range(y):
                if self.board[j] == i:
                    x = abs(y - 1 - i - j)

                    sum += math.pow((math.floor(x / 2)), 2) + (x % 2)
        return sum + self.length * (math.sqrt(self.sofa))


def make_board(length, disks):
    board = [-1] * length
    for i in range(disks):
        board[i] = i
    return board


def solve_distinct_disks(length, n):
    start = DistinctDisk(make_board(length, n))
    fronteir = queue.PriorityQueue()
    li_visited = []
    fronteir.put((start.disk_heuristic(), start))
    solution = 0

    while not fronteir.empty():
        current = fronteir.get_nowait()[1]
        if current.dist_solved():
            solution = current
            break
        li_visited.append((current.move, current))
        for i in current.next_valid_moves():
            ex = 0
            counter = -1
            for j in li_visited:
                counter += 1
                if i.board == j[1].board:
                    ex = 1
                    if i.sofa < j[1].sofa:
                        li_visited[counter] = (i.move, i)
                        fronteir.put((i.disk_heuristic(), i))
                    break

            if ex == 0:
                fronteir.put((i.disk_heuristic(), i))
    rtn = []

    while True:
        if solution.move == None:
            break
        rtn.append((solution.move[1], solution.move[0]))
        solution.move_disk(solution.move[0], solution.move[1])
        for i in li_visited:
            if i[1].board == solution.board:
                solution = i[1]
                break
    return rtn[::-1]
    pass


# x = make_board(6, 3)
# start = DistinctDisk(x)
#
# print(start.get_board())
# print(start.disk_heuristic())
# start.move_disk(2, 3)
# # start.move_disk(1, 2)
# start.move_disk(0, 2)
# start.move_disk(2, 4)
# start.move_disk(4, 5)
#
#
# print(start.get_board())
# print(start.disk_heuristic())

#
# pr = cProfile.Profile()
# pr.enable()
#
# print(solve_distinct_disks(15, 6))
# pr.disable()
#
# pr.print_stats(sort="calls")

############################################################
# Section 4: Feedback
############################################################

# Just an approximation is fine.
feedback_question_1 = 29

feedback_question_2 = """
I found the heuristic for the GridNav to be insufficient. That was terribly misleading.  
"""

feedback_question_3 = """
I liked the nuances of how to store the visited board states based on the problem. I really enjoyed how in the grid 
navigation problem, you could store the visited nodes in a 2 dimensional array as opposed to just a list like the other
problems. 

I liked how after every problem, I was able to approach the subsequent problem with a more efficient plan. If you look
through my code, you can see the evolution of strategy. 

As you can see, by the time I got the the third problem, I had thought so much about the structure of these solutions
that I was able to solve it in a fraction of the time.
"""
