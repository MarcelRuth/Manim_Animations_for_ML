from manim import *

class GraphNeuralNetwork(Scene):
    def construct(self):
        
        node = Dot(radius=0.5, color=RED).shift(3 * DOWN)
        node2 = Dot(radius=0.5, color=RED).shift(1 *DOWN + 2 * RIGHT)
        node3 = Dot(radius=0.5, color=RED).shift(1 *DOWN)
        node4 = Dot(radius=0.5, color=RED).shift(1 * UP)
        
        nodes = [node, node2, node3, node4]
        
        for n in nodes:
            self.play(Create(n), run_time=0.5)
            
        title = Text("A node represents a heavy atom", font_size=24, color=GREEN).shift(3*UP)
        self.add(title)
        self.wait(2)
        
        self.remove(title)
        title = Text("Bonds are represented as edges", font_size=24, color=GREEN).shift(3*UP)
        self.play(Create(title), run_time=2)
        
        
        edge = Line(3 * DOWN, 1 *DOWN)
        edge2 = Line(1 *DOWN, 1*UP)
        edge3 = Line(1 *DOWN, 1 *DOWN + 2 * RIGHT)
        edge4 = Line(1*UP, 1 *DOWN + 2 * RIGHT)
        
        edges = [edge, edge2, edge3, edge4]
        for e in edges:
            self.play(Create(e), run_time=0.5)
        
        self.remove(title)
        title = Text("A molecular graph", font_size=24, color=GREEN).shift(3*UP)
        self.play(Create(title), run_time=2)
        self.wait(2)
        
        self.remove(title)
        title = Text("A feature vector is assigned to \n each node and edge", font_size=24, color=GREEN).shift(3*UP)
        self.play(Create(title), run_time=2)
        
        nfeat = Rectangle(color=DARK_BLUE, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(3 * DOWN + 0.2 + LEFT)
        nfeat2 = Rectangle(color=DARK_BLUE, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(1 * DOWN + 0.2 + LEFT + 2 * RIGHT)
        nfeat3 = Rectangle(color=DARK_BLUE, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(1 * DOWN + 0.2 + LEFT)
        nfeat4 = Rectangle(color=DARK_BLUE, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(1 * UP + 0.2 + LEFT)

        nfeatures = [nfeat, nfeat2, nfeat3, nfeat4]
        
        for nf in nfeatures:
            self.play(Create(nf), run_time=0.5)

        nfeat_text = Text("Node Features", font_size=24, color=GREEN).shift(2*UP + 4 * LEFT)
        nfeat_leg = Rectangle(color=DARK_BLUE, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(2*UP + 2 * LEFT)

        self.add(nfeat_text, nfeat_leg)
        
        efeat = Rectangle(color=BLUE_C, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(2 * DOWN)
        efeat2 = Rectangle(color=BLUE_C, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1)
        efeat3 = Rectangle(color=BLUE_C, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(1 * DOWN + 1.01 * RIGHT)
        efeat4 = Rectangle(color=BLUE_C, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(1.01 * RIGHT)

        efeatures = [efeat, efeat2, efeat3, efeat4]

        for ef in efeatures:
            self.play(Create(ef), run_time=0.5)

        efeat_text = Text("Edge Features", font_size=24, color=GREEN).shift(1*UP + 4 * LEFT)
        efeat_leg = Rectangle(color=BLUE_C, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(1*UP + 2 * LEFT)

        self.add(efeat_text, efeat_leg)

        self.remove(title)
        title = Text("A more sophisticated molecular graph", font_size=24, color=GREEN).shift(3*UP)
        self.play(Create(title), run_time=2)
        self.wait(2)

        dot = Dot(radius=6, color=BLACK)
    
        self.play(FadeIn(dot, run_time=2))
        self.remove(efeat, efeat2, efeat3, efeat4, efeat_leg, efeat_text, nfeat, nfeat2, nfeat3, nfeat4, nfeat_leg, nfeat_text, node, node2, node3, node4, edge, edge2, edge3, edge4, title)
        self.play(FadeOut(dot, run_time=2))
        self.wait(1)

        title = Text("The key idea of most GNNs is \n \'message passing\'", font_size=24, color=GREEN).shift(3*UP)
        self.play(Create(title), run_time=2)
        self.wait(2)
        
        self.remove(title)
        title = Text("Imagine a simple graph \n constituted of 3 nodes and 2 edge \n (ONO for example)", font_size=24, color=GREEN).shift(3*UP)
        self.play(Create(title), run_time=2)
        
        node1 = Dot(radius=0.5, color=RED).shift(2 * LEFT)
        node2 = Dot(radius=0.5, color=RED)
        node3 = Dot(radius=0.5, color=RED).shift(2 * RIGHT) 
        
        for n in [node1, node2, node3]:
            self.play(Create(n), run_time=.5)
        
        edge = Line(2*LEFT, (0,0,0))
        edge2 = Line((0,0,0), 2*RIGHT)
        
        self.play(Create(edge), run_time=.5)
        self.play(Create(edge2), run_time=.5)        
        
        self.remove(title)
        title = Text("For now we only look at \n node features", font_size=24, color=GREEN).shift(3*UP)
        self.play(Create(title), run_time=2)
 
        nfeat = Rectangle(color=DARK_BLUE, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(2 * LEFT + 1 * UP)
        nfeat2 = Rectangle(color=BLUE, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(1 * UP)       
        nfeat3 = Rectangle(color=BLUE_A, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(2 * RIGHT + 1 * UP)
        
        for f in [nfeat, nfeat2, nfeat3]:
            self.play(Create(f), run_time=.5)
        
        self.wait(2)
        
        self.remove(title)
        title = Text("Now they \'talk\' with each other", font_size=24, color=GREEN).shift(3*UP)
        t_counter = MathTex(r"t = 0", font_size=40, color=PINK).shift(2 * UP)
        self.play(Create(t_counter), run_time=1)
        
        arrow1 = CurvedArrow(start_point=nfeat.get_right(), end_point=nfeat2.get_left(), color=ORANGE)
        self.play(Create(arrow1), run_time=2)
        
        arrow2 = CurvedArrow(start_point=nfeat2.get_left(), end_point=nfeat.get_right(), color=ORANGE)
        self.play(Create(arrow2), run_time=2)

        arrow3 = CurvedArrow(start_point=nfeat2.get_right(), end_point=nfeat3.get_left(), color=ORANGE)
        self.play(Create(arrow3), run_time=2)
        
        arrow4 = CurvedArrow(start_point=nfeat3.get_left(), end_point=nfeat2.get_right(), color=ORANGE)
        self.play(Create(arrow4), run_time=2)
        
        self.remove(title)
        title = Text("... and exchange their features", font_size=24, color=GREEN).shift(3*UP)
 
        self.play(Create(title), run_time=2)

        
        # move new features 0.225 to the right, colors are switched
        newfeat = Rectangle(color=BLUE, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(1.775 * LEFT + 1 * UP) 
        newfeat2 = Rectangle(color=BLUE, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(2.225 * RIGHT + 1 * UP)   
        newfeat3 = Rectangle(color=DARK_BLUE, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(0.225 * RIGHT + 1 * UP) 
        newfeat4 = Rectangle(color=BLUE_A, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(0.45 * RIGHT + 1 * UP)  
        
        self.play(FadeOut(arrow1, run_time=0.5))
        self.play(FadeOut(arrow2, run_time=0.5))
        self.play(FadeOut(arrow3, run_time=0.5))
        self.play(FadeOut(arrow4, run_time=0.5))
        
        self.play(FadeIn(newfeat, run_time=0.5))
        self.play(FadeIn(newfeat2, run_time=0.5)) 
        self.play(FadeIn(newfeat3, run_time=0.5))
        self.play(FadeIn(newfeat4, run_time=0.5)) 
         
        transfeat = Rectangle(color=PURPLE, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(2 * LEFT + 1 * UP) 
        transfeat2 = Rectangle(color=PURPLE_A, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(1 * UP)          
        transfeat3 = Rectangle(color=PURPLE_B, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(2 * RIGHT + 1 * UP)   
                        
        self.remove(title)
        title = Text("One timestep has been carried out", font_size=24, color=GREEN).shift(3*UP)
        self.play(Create(title), run_time=2)
        
        self.play(Transform(nfeat, transfeat))
        self.play(Transform(newfeat, transfeat))
        
        self.play(Transform(nfeat2, transfeat2))
        self.play(Transform(newfeat3, transfeat2))
        self.play(Transform(newfeat4, transfeat2))

        self.play(Transform(nfeat3, transfeat3))
        self.play(Transform(newfeat2, transfeat3))
                               
        self.remove(t_counter)
        t_counter = MathTex(r"t = 1", font_size=40, color=PINK).shift(2 * UP)
        self.play(Create(t_counter), run_time=1)
        
        self.remove(title)
        title = Text("One more timestep ...", font_size=24, color=GREEN).shift(3*UP)
        self.play(Create(title), run_time=2)
        
        newfeat5 = Rectangle(color=PURPLE_A, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(1.775 * LEFT + 1 * UP) 
        newfeat6 = Rectangle(color=PURPLE_A, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(2.225 * RIGHT + 1 * UP)   
        newfeat7 = Rectangle(color=PURPLE, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(0.225 * RIGHT + 1 * UP) 
        newfeat8 = Rectangle(color=PURPLE_B, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(0.45 * RIGHT + 1 * UP)  
        
        self.play(FadeIn(newfeat5, run_time=0.5))
        self.play(FadeIn(newfeat6, run_time=0.5)) 
        self.play(FadeIn(newfeat7, run_time=0.5))
        self.play(FadeIn(newfeat8, run_time=0.5)) 

        transfeat4 = Rectangle(color=PURPLE_C, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(2 * LEFT + 1 * UP) 
        transfeat5 = Rectangle(color=PURPLE_D, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(1 * UP)          
        transfeat6 = Rectangle(color=PURPLE_E, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(2 * RIGHT + 1 * UP)  

        self.play(Transform(nfeat, transfeat4))
        self.play(Transform(newfeat5, transfeat4))
        
        self.play(Transform(nfeat2, transfeat5))
        self.play(Transform(newfeat7, transfeat5))
        self.play(Transform(newfeat8, transfeat5))
        
        self.play(Transform(nfeat3, transfeat3))    
        self.play(Transform(newfeat6, transfeat6))

        self.remove(t_counter)
        t_counter = MathTex(r"t = 2", font_size=40, color=PINK).shift(2 * UP)
        self.play(Create(t_counter), run_time=1)

        self.remove(title)
        title = Text("Local information is exchanged and atom embeddings are formed ", font_size=24, color=GREEN).shift(3*UP)
        self.play(Create(title), run_time=2)
        self.wait(2)
        
        self.remove(title)
        title = Text("A molecular embedding can be produced with global pooling operations", font_size=24, color=GREEN).shift(3*UP)
        self.play(Create(title), run_time=2)
        self.wait(2)         

        invis_rectangle = Rectangle(color=BLACK, height=1, width=6)
        brac = Brace(invis_rectangle)
        
        self.play(Create(brac))
                
        glob_feat = Rectangle(color=PURE_RED, height=0.8, width=0.2, grid_xstep=0.2, grid_ystep=0.1).shift(2 * DOWN)
        self.play(Create(glob_feat))   
        
        mol_emb = Text("molecular embedding", font_size=24, color=PURE_RED).shift(2* DOWN + 3 * RIGHT)
        self.play(Create(mol_emb))   
        self.wait(2)
        
        
        dot = Dot(radius=7, color=BLACK)
        self.play(FadeIn(dot, run_time=2))
        self.remove(nfeat, nfeat2, nfeat3, newfeat, newfeat2, newfeat3, newfeat4, newfeat5, newfeat6, newfeat7, newfeat8, transfeat, transfeat2, transfeat3)
        self.remove(title, brac, t_counter, node1, node2, node3, edge, edge2, mol_emb, glob_feat, transfeat4, transfeat5, transfeat6)
        self.play(FadeOut(dot, run_time=2))

        title = Text("simple mathematical functions to describe message passing", font_size=24, color=GREEN).shift(3*UP)
        self.play(Create(title), run_time=2)
        
        eq1 = MathTex(r'h_u^{k} = \sigma (W_{self}^{k}h_u^{k-1} + W_{neigh}^{k} \sum_{\nu \in N (u)} h_v^{k-1} + b^{k})', font_size=40, color=WHITE).shift(1*UP)
        self.play(Create(eq1), run_time=2)
        node_emb = Text("node embedding", font_size=24, color=RED)      
        self.play(Create(node_emb), run_time=2)        

        eq2 = MathTex(r'H^{k} = \sigma (AH^{k-1}W_{neigh}^{k} + H^{k-1}W_{self}^{k})', font_size=40, color=WHITE).shift(1*DOWN)  
        self.play(Create(eq2), run_time=2)
        graph_emb = Text("graph embedding", font_size=24, color=RED).shift(2*DOWN)        
        self.play(Create(graph_emb), run_time=2)   
        
        self.wait(2)            
        

        