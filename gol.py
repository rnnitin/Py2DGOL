import threading
import tkinter as tk
import random as rand
import math

GRID_SIDE = 200
SQUARE_SIDE = 800
BORDER_SIZE = 16
LIFE_SIZE = 12

root = tk.Tk()
canvas = tk.Canvas(root, width=SQUARE_SIDE, height=SQUARE_SIDE)
canvas.pack()

def draw_grid():
    canvas.create_rectangle(BORDER_SIZE, BORDER_SIZE, SQUARE_SIDE - BORDER_SIZE, SQUARE_SIDE - BORDER_SIZE,
            fill="#000000", outline="#7f7f7f")
    for x in range(BORDER_SIZE, SQUARE_SIDE - BORDER_SIZE - 1, LIFE_SIZE):
        for y in range(BORDER_SIZE, SQUARE_SIDE - BORDER_SIZE - 1, LIFE_SIZE):
            canvas.create_rectangle(x+1, y+1, x+LIFE_SIZE-1, y+LIFE_SIZE-1, fill="#000000", outline="#7f7f7f")


def random_lives(x1, y1, x2, y2):
    num_live = int((rand.random() * 0.2 + 0.05) * (math.abs(x2 - x1) / 8 * math.abs(y2 - y1) * 8))
    for i in range (0, num_live):
        for x in range(x1, x2+1, 8):
            print()


class GridMemMgr:
    def __init__(self):
        self.mem_grid = None

draw_grid()
root.mainloop()
