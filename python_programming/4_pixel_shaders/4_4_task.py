import math
import tkinter as tk
import random


def draw(shader, width, height):
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            pos = (width * y + x) * 3
            color = shader(x / width, y / height)
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos:pos + 3] = normalized
    header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
    return header + image


def main(shader):
    label = tk.Label()
    img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()

def noise(*, seed=None, colors):
    if seed != None:
        random.seed(seed)
    return random.choice(colors)
    

def shader(x, y):
    array_of_colors = [(0.5, 0.5, 0.5), (0.6, 0.6, 0.6), (0.8, 0.8, 0.8), (1, 1, 1), (0, 0, 0)]
    res = noise(colors = array_of_colors)
    return res[0], res[1], res[2]


main(shader)
