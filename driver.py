from cv2 import imread
from pyautogui import screenshot,locateAll,click,write,locateOnScreen
from pyscreeze import ImageNotFoundException
from sudoku_solver import solve_sudoku
from time import sleep
from pprint import pprint

BOARD_LEFT = 171
BOARD_TOP = 313
BOARD_SIZE = 600
CELL_SIZE = BOARD_SIZE/9
CONFIDENCE = 0.875

new_game_location = (855,180)
extreme_location = (740,650)

def board_maker():
    board_matrix = [[-1 for _ in range(9)] for __ in range(9)]

    click(locateOnScreen('blank_cell.png',confidence=0.6))
    sleep(0.1)
    screenshot('screenshot.png',(BOARD_LEFT,BOARD_TOP,BOARD_SIZE,BOARD_SIZE))
    ss = imread('screenshot.png')

    for num in range(1,10):
        for c in ['white','blue']:
            num_img = imread(f"Number_Images/{num}_{c}.png")
            try:    arr = list(locateAll(num_img,ss,confidence=CONFIDENCE))
            except ImageNotFoundException:  continue
            for i in range(len(arr)):
                box = arr[i]
                x = round(box.left/CELL_SIZE)
                y = round(box.top/CELL_SIZE)
                arr[i] = (x,y)
            arr = list(set(arr))
            for x,y in arr:
                if board_matrix[y][x]==-1:
                    board_matrix[y][x] = num
    
    return board_matrix

def solve_and_fill():
    board = board_maker()
    print("Board made:")
    pprint(board)
    to_fill = []

    for row in range(9):
        for col in range(9):
            if board[row][col]==-1: to_fill.append((row,col))
    
    print("Solving board")
    solve_sudoku(board)
    print("Solved board:")
    pprint(board)
    print("Solved, filling")

    for row,col in to_fill:
        y = BOARD_TOP+CELL_SIZE//2+CELL_SIZE*row
        x = BOARD_LEFT+CELL_SIZE//2+CELL_SIZE*col
        
        click(x,y)
        write(str(board[row][col]))

input("Press enter to start")

while True:
    solve_and_fill()
    print("Filled, starting new game")
    sleep(1)
    click(new_game_location)
    sleep(1)
    click(extreme_location)
    print("Game loaded, waiting 5 seconds")
    sleep(5)
    print("Wait time complete\n")