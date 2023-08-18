from turtle import width
from manim import *
class NeuralNetwork(Scene):
    def construct(self):
        # place a dot at the origin
        dot = Dot(radius=0.2, color=RED).shift(2*LEFT)
        text = Text("One neuron", font_size=24, color=BLUE).shift(3.5*LEFT)
        # Add the dot to the screen
        self.add(dot)
        self.play(Create(text))
        self.wait(1.0)
        
        for i in range(11):
            dot = Dot(radius=0.2, color=RED).shift(1 * LEFT + i/2 * UP + 2.5*DOWN)
            # Add all to the screen
            self.add(dot)
            self.play(Create(dot), run_time=0.2)
            
        for i in range(11):
            dot = Dot(radius=0.2, color=RED).shift(i/2 * UP + 2.5*DOWN)
            # Add all to the screen
            self.add(dot)
            self.play(Create(dot), run_time=0.2)
        
        for i in range(11):
            dot = Dot(radius=0.2, color=RED).shift(1 * RIGHT + i/2 * UP + 2.5*DOWN)
            # Add all to the screen
            self.add(dot)
            self.play(Create(dot), run_time=0.2)
            
        self.remove(text)
        many_neurons = Text("Many neurons", font_size=24, color=BLUE).shift(3.5*LEFT)
        self.play(Create(many_neurons), run_time=1)
        self.wait(2.0)
        self.remove(many_neurons)

        many_connections = Text("Many connections", font_size=24, color=BLUE).shift(4*LEFT)
        self.play(Create(many_connections), run_time=1)
        self.wait(2.0)
        
        #loop through all neuron positions
        
        for i in range(11):
            START = 2 * LEFT
            END = 1 * LEFT + i/2 * UP + 2.5*DOWN
            line = Line(START,END, color=DARK_BLUE)
            self.play(Create(line, run_time=0.01))
        
        for x in [0, 1, 2]:
            for y in range(11):
                if x < 2: #last layer needs no automated connections
                    START = 1 * LEFT + x * RIGHT + y/2 * UP + 2.5*DOWN
                    #loop through all connections of the given neuron
                    for i in range(11):
                        # 1 + x is next layer
                        END = 1 * LEFT + (1 + x) * RIGHT + i/2 * UP + 2.5*DOWN
                        line = Line(START,END, color=DARK_BLUE)
                        self.play(Create(line, run_time=0.01))

         


        self.remove(many_connections)      
        output_question = Text("What task \n do we want to solve?", font_size=24, color=GREEN).shift(5*LEFT)
        self.play(Create(output_question), run_time=2)
        self.wait(1.0)

        self.remove(output_question)
        output_question = Text("Regression!", font_size=24, color=GREEN).shift(5*LEFT)
        self.play(Create(output_question), run_time=2)
        self.wait(1.0)
  
        dot = Dot(radius=0.2, color=RED).shift(2 * RIGHT)
        self.add(dot)
        self.play(Create(dot))
        
        for i in range(11):
            START = 1 * RIGHT + i/2 * UP + 2.5*DOWN
            END = 2 * RIGHT
            line = Line(START,END, color=DARK_BLUE)
            self.play(Create(line, run_time=0.01))   
        
        self.remove(output_question)
        output_node = Text("The output neuron ", font_size=24, color=BLUE).shift(4*RIGHT)
        input_neurons = Text("The input neuron", font_size=24, color=BLUE).shift(4*LEFT)
        self.play(Create(input_neurons), run_time=1)     
        self.play(Create(output_node), run_time=1)
        self.wait(1.0)  
        
        title = Text("A simple feed-forward neural network", font_size=24, color=GREEN).shift(3*UP)
        self.add(title)
        self.play(Create(title), run_time=3)
        self.wait(2.0)        
        
        