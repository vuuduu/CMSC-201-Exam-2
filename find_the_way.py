"""
File:         find_the_way.py
Author:       Vu Nguyen
Date:         11/22/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  Objective: modified the find_the_way_out function to checks
              all four direction in order to find a path that go out of
              bound.
"""

import sys
import random

ALLOWED = '_'
FORBIDDEN = '*'
BAD = 'b'


def create_map(x, y, p):
    """
    :param x: the number of rows of the grid
    :param y: the number of cols of the grid
    :param p: the probability of a forbidden space
    :return: the grid, the starting location
    """
    the_grid = [[FORBIDDEN if random.random() < p else ALLOWED for j in range(y)] for i in range(x)]
    x = random.randint(0, x - 1)
    y = random.randint(0, y - 1)
    the_grid[x][y] = 's'
    return the_grid, [x, y]


def find_the_way_out(the_grid, starting_position, step=0):
    """
    :param the_grid: this is a 2d grid, either the positions will be ALLOWED which is a space, or "*" or "s".  s is the starting position passed as a list
        and * is
    :param starting_position:  the starting list/tuple coordinate for the starting position.
    :return: True if there is a way out, False if not

    You need to implement this function
    You are permitted to add helper functions but you shouldn't change the signature (name and parameters) of this function.
    """
    cant_move = True
    x, y = starting_position
    the_grid[x][y] = str(step)
    # This checks for out of bound condition
    if x - 1 < 0 or y - 1 < 0 or x + 1 > len(the_grid) - 1 or y + 1 > len(the_grid[x]) - 1:
        return True
    else:
        # Go Up
        if the_grid[x - 1][y] == ALLOWED:
            if find_the_way_out(the_grid, (x - 1, y), step + 1):
                return True
            the_grid[x - 1][y] = BAD

        # Go right
        if the_grid[x][y + 1] == ALLOWED:
            if find_the_way_out(the_grid, (x, y + 1), step + 1):
                return True
            the_grid[x][y + 1] = BAD

        # Go Left
        if the_grid[x][y - 1] == ALLOWED:
            if find_the_way_out(the_grid, (x, y - 1), step + 1):
                return True
            the_grid[x][y - 1] = BAD

        # Go Down
        if the_grid[x + 1][y] == ALLOWED:
            if find_the_way_out(the_grid, (x + 1, y), step + 1):
                return True
            the_grid[x + 1][y] = BAD

        if cant_move:
            the_grid[x][y] = BAD
            return False


def display(the_grid):
    """
        This should display the grid on the screen.
    :param the_grid: the 2d grid.
    """
    print('\n'.join(''.join([str(x).ljust(3) for x in the_grid[i]]) for i in range(len(the_grid))))


if __name__ == '__main__':
    if len(sys.argv) == 5:
        seed = int(sys.argv[1])
        x_dimension = int(sys.argv[2])
        y_dimension = int(sys.argv[3])
        probability = float(sys.argv[4])
    else:
        seed = input('What is the seed (enter a string): ')
        x_dimension = int(input('Enter the x dimension: '))
        y_dimension = int(input('Enter the y dimension: '))
        probability = float(input('Enter a float between 0 and 1 to represent the probability of a forbidden space: '))

    random.seed(seed)

    while input('Again? ').strip().lower() == 'yes':
        the_grid, starting = create_map(x_dimension, y_dimension, probability)
        display(the_grid)
        print(find_the_way_out(the_grid, starting))
        display(the_grid)
