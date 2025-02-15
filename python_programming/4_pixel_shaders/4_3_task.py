import math
import tkinter as tk


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


def shader(x, y):
    r = 0.1
    x_pos = 0.5
    y_pos = 0.5
    pos = (x - x_pos) ** 2 + (y - y_pos) ** 2
    if pos <= r:
        radians = math.atan2(y - 0.5, x - 0.5)
        degrees = math.degrees(radians)
        if (30 > degrees > -30) or ((x - 0.60) ** 2 + (y - 0.30) ** 2 <= 0.003):
            return 0, 0, 0
        return 1, 1, 0
    return 0, 0, 0


main(shader)
