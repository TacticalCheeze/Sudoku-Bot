# Sudoku-Bot
By: William Romine

This is a Sudoku auto-completer written in python. It reads in a grid from a local file and displays the solved grid via a GUI.

How it works(In-depth):
  This program reads in a sudoku grid as a csv from "grid.txt". I included an example of the format so see that for the input format.

  It reads it in, line by line. To solve the puzzle, it uses a technique that closely resembles Python enthusiast's method (as seen here= https://www.youtube.com/watch?v=PZJ5mjQyxR8&list=PL1_f9e9q_vOV0JtqZ2lvWMp1abL5NLWOz&index=1). This method incorporates backtracking and recursion and was really fun to implement. It then uses matplotlib to display the result with a GUI.
    
   I plan to make a new way to input the grid that will be much cooler. You will upload an image of the grid and I'll use Keras or something to automagically get the numbers from the puzzle.
    
P.S. If anyone has any improvments or ideas feel free, and anyone can use this for whatever.

