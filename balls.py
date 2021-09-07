#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:32:50 2021

@author: aleksejlipavskij
"""

import tkinter as tk
import random

HEIGHT = 200
WIDTH = 300

class Ball:
    def __init__(self):
        self.R = random.randint(3, 11)
        self.x = random.randint(self.R, WIDTH - self.R)
        self.y = random.randint(self.R, HEIGHT - self.R)
        
        self.dx = random.randint(1, 15)
        self.dy = random.randint(1, 16)
        self.color = random.choice(['blue', 'green', 'red', 'brown'])
        self.id = canvas.create_oval(
                                self.x - self.R,
                                self.y - self.R,
                                self.x + self.R,
                                self.y + self.R,
                                fill=self.color
                                )
    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x - self.R <= 0 or self.x + self.R >= WIDTH:
            self.dx = -self.dx
        if self.y - self.R <= 0 or self.y + self.R >= HEIGHT:
            self.dy = -self.dy
    def show(self):
        canvas.move(self.id, self.dx, self.dy)


def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(30, tick)


def main():
    global root, canvas, balls
    
    root = tk.Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    canvas = tk.Canvas(root)
    canvas.pack(anchor="nw", fill=tk.BOTH)
    canvas.bind("<Button-1>")
    balls = [Ball() for i in range(45)]
    tick()
    root.mainloop()
    


if __name__ == "__main__":
    main()

