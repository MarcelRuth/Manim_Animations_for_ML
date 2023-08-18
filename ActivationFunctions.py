from tkinter import RIGHT
from turtle import down

from pandas import array
from manim import *

import numpy as np

class ActivationFunctions(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3, .5],
            y_range=[-2, 2, 1],
            x_axis_config={"numbers_to_include": [-3, -2, -1, 0, 1, 2, 3]},
            y_axis_config={"numbers_to_include": [-2, -1, 0, 1, 2]},
            tips=True
        )
        axes_labels=axes.get_axis_labels()
        # Get the graph of a simple functions
        graph = axes.plot(lambda x: x if x >= 0 else 0.0, color=RED) #ReLU
        graph_2 = axes.plot(lambda x: 1/(1+np.exp(-x)), color=GREEN) #sigmoid function
        graph_3 =axes.plot(lambda x: np.tanh(x), color=BLUE) #tanh function
        
        # Set up its label
        # ReLU
        graph_label = axes.get_graph_label(
            graph, x_val=1, direction= 10 * LEFT + 5 * UP,
           label=r'ReLU(x) = max(0,x)', color=RED
        )

        # Sigmoid
        graph_label_2 = axes.get_graph_label(
            graph_2, x_val=1, direction= 9 * RIGHT + 10 * DOWN,
           label=r'Sigmoid(x) = \frac{1}{1+e^{-x}}', color=GREEN
        )

        # Tanh
        graph_label_3 = axes.get_graph_label(
            graph_3, x_val=1, direction= 11 * LEFT + 10 * DOWN,
           label=r'tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}', color=BLUE
        )

        # Graph the axes components together
        axes_group = VGroup(axes, axes_labels)
        
        # Animate
        self.play(Create(axes_group), run_time=2) #draw axes
        self.wait(0.25)
        
        #draw graph and labels
        self.play(Create(graph), run_time=3)
        self.play(Write(graph_label), run_time=2)
        self.play(Create(graph_2), run_time=3)
        self.play(Write(graph_label_2), run_time=2)
        self.play(Create(graph_3), run_time=3)
        self.play(Write(graph_label_3), run_time=2)           