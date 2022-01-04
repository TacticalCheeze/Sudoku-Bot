"""
sudokuSolver.py
William Romine
This file reads in a sudoko grid from "grid.txt" as a csv, solves it, then displays the answer using a GUI(matplotlib)
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],  # Placeholder grid (serves no real purpose but the grid must exist in global)
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def readGrid():
    """
    Reads in desired grid from grid.txt and stores it in global grid var
    :return:
    """
    with open("grid.txt") as f:
        global grid
        grid = []  # empty grid
        for i in range(0, 9):
            row = f.readline().split(",")
            for j in range(0, 9):
                row[j] = int(row[j])
            grid.append(row)


def possible(row, column, number):
    """
    Finds first possible number for that square
    :param row: row index in game, used to check
    :param column: column index in game, used to check
    :param number: the number it is trying to put in square
    :return: returns false if number cannot go in square, true otherwise
    """
    global grid
    # Is the number in the row?
    for i in range(0, 9):
        if grid[row][i] == number:
            return False

    # Is the number in the column?
    for i in range(0, 9):
        if grid[i][column] == number:
            return False

    # Is the number in the square?
    x0 = (column // 3) * 3  # Get x starting position
    y0 = (row // 3) * 3  # Get y starting position
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == number:
                return False

    return True


def display():
    """
    Displays solved grid using matplotlib
    :return:
    """
    figure = plt.figure(num="Sudoku Solver")
    axes = figure.add_subplot(111)
    my_colormap = ListedColormap(["white"])  # Create a color map of only white for background
    axes.matshow(grid, cmap=my_colormap)  # Plot a color grid using our colormap of only white
    for (i, j), z in np.ndenumerate(grid):  # Put the answers in the boxes and make a gid of them using bbox
        axes.text(j, i, "{:0.0f}".format(z), ha="center", va="center", bbox=dict(boxstyle="square,pad=0.8",
                                                                                 facecolor="white", edgecolor="0.3"))
    axes.xaxis.set(ticks=range(0))  # Get rid of ticks (optional)
    axes.yaxis.set(ticks=range(0))
    plt.title("Your Sudoku Answer")
    plt.show()


def solve():
    """
    Solves each zero square, if it runs into an unsolvable puzzle, it uses recursion to backtrack and try another
    solution. It also checks for other possible solutions after it is done with the first one.
    :return:
    """
    global grid
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:  # No need to solve anything but 0's (blanks)
                for number in range(1, 10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()  # Recursion yay
                        grid[row][column] = 0

                return

    #print(np.matrix(grid))  # Print answer to console
    display()


def main():
    readGrid()
    solve()


if __name__ == "__main__":
    main()
