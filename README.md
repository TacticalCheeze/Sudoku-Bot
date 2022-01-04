# Sudoku-Bot
By: William Romine
This is a Sudoku auto-completer written in python. It reads in a grid from a local file and displays the solved grid via a GUI.

How it works(In-depth):
  This program reads in a sudoku grid as a csv from "grid.txt". I included an example of the format but I will provide another example here:
  
  \n = new line
  
0,0,0,8,0,0,4,0,0\n
7,6,8,0,3,0,0,0,9\n
0,0,0,0,0,2,0,7,0\n
0,4,5,9,0,0,0,0,0\n
1,0,0,0,0,0,0,0,4\n
0,0,0,0,0,8,5,6,0\n
0,3,0,7,0,0,0,0,0\n
5,0,0,0,9,0,8,2,3\n
0,0,9,0,0,1,0,0,0\n

  It reads it in, line by line. To solve the puzzle, it uses a technique that closely resembles Python enthusiast's method (as seen here= https://www.youtube.com/watch?v=PZJ5mjQyxR8&list=PL1_f9e9q_vOV0JtqZ2lvWMp1abL5NLWOz&index=1). This method incorporates backtracking and recursion and was really fun to implement. It then uses matplotlib to display the result with a GUI.
    
    I plan to make a new way to input the grid that will be much cooler. You will upload an image of the grid and I'll use Keras or something to automagically get the numbers from the puzzle.
