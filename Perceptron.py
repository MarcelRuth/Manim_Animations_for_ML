from tkinter import RIGHT
from turtle import down

from pandas import array
from manim import *

import numpy as np

class Perceptron(Scene):
    def construct(self):

        func = MathTex(r"f(x) = ax", font_size=24, color=BLUE)
        self.play(Create(func), run_time=2)
        self.wait(1.0)
        self.remove(func)
        
        func = MathTex(r"g(f(x)) = \lambda f(x)", font_size=24, color=BLUE)
        self.play(Create(func), run_time=2)
        title = Text('A nested function', font_size=24, color=GREEN).shift(3*UP)
        self.play(Create(title), run_time=1)
        self.wait(2.0)
        self.remove(func)
        self.remove(title)
        
        func = MathTex(r"h(g(f(x))) = \alpha g(f(x)) = \alpha \lambda a x", font_size=24, color=BLUE)
        self.play(Create(func), run_time=2)
        title = Text('A nested-nested function', font_size=24, color=GREEN).shift(3*UP)
        self.play(Create(title), run_time=1)
        self.wait(2.0)
        self.remove(func)
        self.remove(title)
        
        func = MathTex(r"f(x) = f_L(f_{L-1}(...(f_1(x))...))", font_size=24, color=BLUE)
        self.play(Create(func), run_time=2)
        title = Text('Nested many times', font_size=24, color=GREEN).shift(3*UP)
        self.play(Create(title), run_time=1) 
        self.wait(2.0)
        self.remove(title)
        self.remove(func)
        
        title = Text('Represent function(s) as nodes', font_size=24, color=GREEN).shift(3*UP)
        self.play(Create(title), run_time=1) 
        dot = Dot(radius=1, color=BLUE)

        self.wait(2.0)
        func = MathTex(r"...", font_size=24, color=BLUE).shift(1.5 * LEFT)
        self.play(Create(func), run_time=2)
        for i in range(5):
            dot = Dot(radius=0.2, color=BLUE).shift(1 * LEFT + i/2 * RIGHT)
            self.play(Create(dot), run_time=1)
        func = MathTex(r"...", font_size=24, color=BLUE).shift(1.5 * RIGHT)
        self.play(Create(func), run_time=2)
        self.wait(2.0) 