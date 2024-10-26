# Sudoku-Autoplay-Bot

A bot to automatically solve sudoku puzzles on the sudoku.com interface.

The bot automatically detects the given sudoku grid and solves it uses standard backtracking. The grid is then filled out using the PyAutoGui library. A new game is automatically started after 1 finishes.

Note: the bot has been calibrated to play on sudoku.com only on 1 local machine. There are constant values such as resolution and paths which change from device to device. These changes need to be made to ensure the program runs without issues on other devices.