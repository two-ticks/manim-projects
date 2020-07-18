from manimlib.imports import *
import math

class Cosine(GraphScene):
    
    CONFIG = {
       "plane_kwargs" : { 
        "x_line_frequency" : 1,
        "y_line_frequency" :1,
       },
        "function" : lambda x : np.cos(x), 
        "function_color" : BLUE,
        "axes_color": WHITE,
        "center_point" : 0,
        "x_axis_width": 20,
        "y_axis_height": 8,
        "x_min" : -10,
        "x_max" :  10,
        "y_min" :  -4,
        "y_max" :   4,
        "graph_origin" : ORIGIN ,
        "x_labeled_nums" :range(-6,6+1,1),
        "y_labeled_nums" :range(-3,3+1,1),
       
    }
    def construct(self):
      # Number Plane and Axes
        my_plane = NumberPlane(**self.plane_kwargs)
        self.add(my_plane)
        self.setup_axes(animate=False)
   
      # GraphOfCosine  
        func_graph = self.get_graph(
            self.function,
            self.function_color,
        )
        
        text1=TextMobject("\\Large y = cos(x)")
        tex1=TextMobject("\\Large y = cos(x)")
        te1=TextMobject("\\Large y = cos(x)")
        t1=TextMobject("\\Large y = cos(x)")
        t=TextMobject("\\Large y = cos(x)")
        tex1.move_to(np.array([3,3,0]))
        text1.move_to(np.array([3,3,0]))
        te1.move_to(np.array([3,3,0]))
        t1.move_to(np.array([3,3,0]))
        t.move_to(np.array([3,3,0]))
        
        self.play(Write(text1),run_time=3)
        self.wait()
        self.play(
            ShowCreation(func_graph),run_time=2
        )
        
        p1=Dot(color=RED,radius=0.1)
        p1.move_to(np.array([0,1,0]))
        self.add(p1)
        
        # cos(x-2)
        
        text2=TextMobject("\\Large y = cos(x-2)")
        text2.move_to(np.array([3,3,0]))
        self.play(Transform(text1,text2))
        
        self.play(ApplyMethod(func_graph.shift,2*RIGHT),ApplyMethod(p1.shift,2*RIGHT),run_time=2)
        self.wait()
        self.remove(text1)
        self.play(Transform(text2,tex1))
       
        self.play(ApplyMethod(func_graph.shift,2*LEFT),ApplyMethod(p1.shift,2*LEFT),run_time=2)
        self.wait()
        
        # cos(x+2)
        
        self.remove(text2)
        text3=TextMobject("\\Large y = cos(x+2)")
        text3.move_to(np.array([3,3,0]))
        self.play(Transform(tex1,text3))                
        self.play(ApplyMethod(func_graph.shift,2*LEFT),ApplyMethod(p1.shift,2*LEFT),run_time=2)
        self.wait()
        self.remove(tex1)
        self.play(Transform(text3,te1))        
        self.play(ApplyMethod(func_graph.shift,2*RIGHT),ApplyMethod(p1.shift,2*RIGHT),run_time=2)
        self.wait()
        
        # cos(x)+2
        
        self.remove(text3)
        text4=TextMobject("\\Large y = cos(x)+2")
        text4.move_to(np.array([3,3,0]))
        self.play(Transform(te1,text4))  
        self.play(ApplyMethod(func_graph.shift,2*UP),ApplyMethod(p1.shift,2*UP),run_time=2)              
        self.wait()
        self.remove(te1)
        self.play(Transform(text4,t1))
        self.play(ApplyMethod(func_graph.shift,2*DOWN),ApplyMethod(p1.shift,2*DOWN),run_time=2)        
        self.wait()
        
        # cos(x)-2
        
        self.remove(text4)
        text5=TextMobject("\\Large y = cos(x)-2")
        text5.move_to(np.array([3,3,0]))
        self.play(Transform(t1,text5))
        self.play(ApplyMethod(func_graph.shift,2*DOWN),ApplyMethod(p1.shift,2*DOWN),run_time=2)                
        self.wait()
        self.remove(t1)
        self.play(Transform(text5,t))
        self.play(ApplyMethod(func_graph.shift,2*UP),ApplyMethod(p1.shift,2*UP),run_time=2)
        self.wait()
        
        
