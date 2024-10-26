import pytesseract as pyt
from cv2 import imread,imshow,waitKey,imwrite
from pyautogui import screenshot
from time import sleep

BOARD_LEFT = 171
BOARD_TOP = 313
BOARD_SIZE = 600
CELL_SIZE = round(BOARD_SIZE/9)
MARGIN = 5

pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def get_board():
    input("Press enter to start 5 second timer")
    sleep(5)

    screenshot('screenshot.png',(BOARD_LEFT,BOARD_TOP,BOARD_SIZE,BOARD_SIZE))
    ss = imread('screenshot.png')

    for row in range(9):
        for col in range(9):
            x = col*CELL_SIZE
            y = row*CELL_SIZE
            cell_image = ss[y+MARGIN:y + CELL_SIZE-MARGIN, x+MARGIN: x + CELL_SIZE-MARGIN]
            number = pyt.image_to_string(cell_image,config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')
            number.strip()
            if number=='': number = '0'
            number = int(number)
            print(number,end=',')
            imshow('scr',cell_image)
            waitKey(0)
        print()

def save_num_image(path,x,y):
    screenshot('screenshot.png',(BOARD_LEFT,BOARD_TOP,BOARD_SIZE,BOARD_SIZE))
    ss = imread('screenshot.png')
    cell_image = ss[y+MARGIN:y + CELL_SIZE-MARGIN, x+MARGIN: x + CELL_SIZE-MARGIN]
    imwrite(path,cell_image)
    
for num in range(7,10):
    for c in ['white','blue']:
        name = f"{num}_{c}"
        print(name)
        r,c = map(int,input().split(','))
        print()
        save_num_image(name+'.png',c*CELL_SIZE,r*CELL_SIZE)
