from manimlib.imports import *
import math
class Fn(Scene):
    def construct(self):
        text = VGroup(
                TextMobject("A 2 × 2 non-singular matrix with repeated eigen values is given as $ \\begin{bmatrix} x & -3 \\\\ 3 & 4 \\end{bmatrix} $ where x is a real positive number, then the value of x is "),
                TextMobject("GATE-2021 ECE").set_color(BLUE)
            )
        text.arrange(DOWN)\
                .scale(0.7)\
                .set_fill(opacity=0)

        screen = Rectangle(
                            width=FRAME_WIDTH,
                            height=FRAME_HEIGHT
                )

        for position,t in zip([LEFT,RIGHT],text):
            t_c = t.copy()
            t.next_to(screen,position,buff=0)
            t.set_y(t_c.get_y())

        def show_text(text_):
            t1,t2 = text_
            t1.set_x(0)
            t2.set_x(0)
            text_.set_fill(opacity=1)
            return text_

        def disappear_text(text_):
            for position,t in zip([RIGHT,LEFT],text_):
                t_c = t.copy()
                t.next_to(screen,position,buff=0)
                t.set_y(t_c.get_y())
                t.set_fill(opacity=0)
            return text_

        self.play(ApplyFunction(show_text,text))
        self.wait(4)
        self.remove(text[1])

        text1 = VGroup(
        			   TextMobject("By definition, $\\boxed{AX=\\lambda X}$").set_color(ORANGE),
        			   #TextMobject("$sin(A+B)+sin(A-B) = 2sin(A)cos(B)$"),
        	           TextMobject("$  \\begin{bmatrix} x & -3 \\\\ 3 & 4 \\end{bmatrix} X = \\lambda X $"),
        	           TextMobject("$ \\begin{bmatrix} x & -3 \\\\ 3 & 4 \\end{bmatrix} X - \\lambda X = [O] $"),
        	           TextMobject("$ \\bigg(\\begin{bmatrix} x & -3 \\\\ 3 & 4 \\end{bmatrix}  - \\lambda I \\bigg) X = O $"),
        	           #TextMobject("$cos(A+B)+cos(A-B) = 2cos(A)cos(B)$"),
        	           TextMobject("$ \\begin{vmatrix} \\begin{bmatrix} x & -3 \\\\ 3 & 4 \\end{bmatrix} -\\begin{bmatrix}  \\lambda & 0 \\\\ 0 &  \\lambda  \\end{bmatrix} \\end{vmatrix}   = 0 $"),
        	           # TextMobject("$ \\begin{vmatrix} \\begin{bmatrix} x -\\lambda & -3 \\\\ 3 & 4-\\lambda \\end{bmatrix} \\end{vmatrix}   = 0 $")
        	           )
        text1.scale(0.8).shift(3*UP)
        
        self.play(Transform(text[0],text1[0]))
        self.wait(2)
        #text4 = TextMobject("$|A-\\lambda I|=0$")
        #text4.next_to(text,DOWN).set_color(YELLOW)
        #self.play(Write(text4))
        #self.wait(2)
        #self.remove(text4)
        
        for i in range (1,5): # writing loop
            text1[i].next_to(text1,DOWN) #.set_color(YELLOW)
            self.play(Write(text1[i]))
            self.wait(1)
        
        self.wait(1)
        for i in range (0,5): # writing loop
            #text1[i].next_to(text1,DOWN) #.set_color(YELLOW)
            self.remove(text1[i])
            #self.play(Write(text1[i]))
            #self.wait(2)
        #self.play(FadeOut(text),FadeOut(text1))
        #self.play(Transform(text1,text1[7]))
        self.remove(text[0])
        #self.add(text1)

        text2 = VGroup(TextMobject("$ \\begin{vmatrix}  x -\\lambda & -3 \\\\ 3 & 4-\\lambda  \\end{vmatrix}  = 0 $"),
        	           TextMobject("$(x -\\lambda)(4 -\\lambda)-(3)(-3)=0 $"),
        	           TextMobject("$\\lambda^2-(4+x)\\lambda +4x +9=0$").set_color(BLUE)
        	           #TextMobject("$\\lambda^2-(4+x)\\lambda +4x +9=0$"),
    )
        text2.scale(0.9).shift(UP)
        self.play(Write(text2[0]))
        for j in range (1,3): # writing loop
            text2[j].next_to(text2,DOWN) #.set_color(YELLOW)
            self.play(Write(text2[j]))
            self.wait(2)
        self.wait(1)    
        for i in range (0,3): # writing loop
            #text1[i].next_to(text1,DOWN) #.set_color(YELLOW)
            self.remove(text2[i])
            #self.play(Write(text1[i]))
            #self.wait(2)
        #self.play(FadeOut(text),FadeOut(text1))
        #self.play(Transform(text1,text1[7]))
        #self.remove(text2[0])    
        #self.wait(3)
        text3 = VGroup(
        	           TextMobject("for real and repeated $\\lambda$, $b^2-4ac = 0$"),
        	           TextMobject("$(4+x)^2-4(4x+9) = 0$"),
        	           TextMobject("$x^2-8x-20 = 0$"),
        	           TextMobject("$(x-10)(x+2) = 0$"),
        	           TextMobject("x = 10,-2"),
        	           TextMobject("x=10(positive)"),
                       TextMobject("$\\boxed{x=10}$").set_color(YELLOW))
        text3.scale(0.8).shift(2*UP)
        self.play(Write(text3[0]))
        for k in range (1,6): # writing loop
            text3[k].next_to(text3,DOWN) #.set_color(YELLOW)
            self.play(Write(text3[k]))
            self.wait(1)
        self.wait(1)    
        self.play(Write(text3[6].scale(1.5).next_to(text3,DOWN)))
        self.wait(3)
        
