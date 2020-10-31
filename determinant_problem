from manimlib.imports import *
import math
class Fn(Scene):
    def construct(self):
        text = VGroup(
                TextMobject("$\\begin{vmatrix} sin(\\theta) & cos(\\theta) & sin(2\\theta) \\\\ sin(\\theta + \\frac{2\\pi}{3}) & cos(\\theta + \\frac{2\\pi}{3}) & sin(2\\theta + \\frac{4\\pi}{3}) \\\\ sin(\\theta - \\frac{2\\pi}{3}) & cos(\\theta - \\frac{2\\pi}{3}) & sin(2\\theta - \\frac{4\\pi}{3}) \\end{vmatrix}$"),
                TextMobject("Hmm, let's give this a try!!").set_color(YELLOW)
            )
        text.arrange(DOWN)\
                .scale(1.2)\
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
        			   TextMobject("$\\Delta = \\begin{vmatrix} sin(\\theta) & cos(\\theta) & sin(2\\theta) \\\\ sin(\\theta + \\frac{2\\pi}{3}) & cos(\\theta + \\frac{2\\pi}{3}) & sin(2\\theta + \\frac{4\\pi}{3}) \\\\ sin(\\theta - \\frac{2\\pi}{3}) & cos(\\theta - \\frac{2\\pi}{3}) & sin(2\\theta - \\frac{4\\pi}{3}) \\end{vmatrix}$"),
        			   #TextMobject("$sin(A+B)+sin(A-B) = 2sin(A)cos(B)$"),
        	           TextMobject("$sin(\\theta + \\frac{2\\pi}{3})+sin(\\theta - \\frac{2\\pi}{3})=2sin(\\theta)cos(\\frac{2\\pi}{3})$"),
        	           TextMobject("$sin(\\theta + \\frac{2\\pi}{3})+sin(\\theta - \\frac{2\\pi}{3})=2sin(\\theta)(\\frac{-1}{2}) $"),
        	           TextMobject("$\\boxed{sin(\\theta + \\frac{2\\pi}{3})+sin(\\theta - \\frac{2\\pi}{3})=-sin(\\theta)} $"),
        	           #TextMobject("$cos(A+B)+cos(A-B) = 2cos(A)cos(B)$"),
        	           TextMobject("$cos(\\theta + \\frac{2\\pi}{3})+cos(\\theta - \\frac{2\\pi}{3})=2cos(\\theta)cos(\\frac{2\\pi}{3})$"),
        	           TextMobject("$cos(\\theta + \\frac{2\\pi}{3})+cos(\\theta - \\frac{2\\pi}{3})=2cos(\\theta)(\\frac{-1}{2}) $"),
        	           TextMobject("$\\boxed{cos(\\theta + \\frac{2\\pi}{3})+cos(\\theta - \\frac{2\\pi}{3})=-cos(\\theta)} $"),
        	           TextMobject("$sin(2\\theta + \\frac{4\\pi}{3})+sin(2\\theta - \\frac{4\\pi}{3})=2sin(2\\theta)cos(\\frac{4\\pi}{3})$"),
        	           TextMobject("$sin(2\\theta + \\frac{4\\pi}{3})+sin(2\\theta - \\frac{4\\pi}{3})=2sin(2\\theta)(\\frac{-1}{2}) $"),
        	           TextMobject("$\\boxed{sin(2\\theta + \\frac{4\\pi}{3})+sin(2\\theta - \\frac{4\\pi}{3})=-sin(2\\theta)}$"),
        	           TextMobject("$\\begin{vmatrix} sin(\\theta) & cos(\\theta) & sin(2\\theta) \\\\ sin(\\theta + \\frac{2\\pi}{3}) & cos(\\theta + \\frac{2\\pi}{3}) & sin(2\\theta + \\frac{4\\pi}{3}) \\\\ sin(\\theta - \\frac{2\\pi}{3}) & cos(\\theta - \\frac{2\\pi}{3}) & sin(2\\theta - \\frac{4\\pi}{3}) \\end{vmatrix}$"),
        	           TextMobject("$\\begin{vmatrix} sin(\\theta) & cos(\\theta) & sin(2\\theta) \\\\ sin(\\theta + \\frac{2\\pi}{3}) & cos(\\theta + \\frac{2\\pi}{3}) & sin(2\\theta + \\frac{4\\pi}{3}) \\\\ sin(\\theta - \\frac{2\\pi}{3})+sin(\\theta + \\frac{2\\pi}{3}) & cos(\\theta - \\frac{2\\pi}{3})+cos(\\theta + \\frac{2\\pi}{3}) & sin(2\\theta - \\frac{4\\pi}{3})+sin(2\\theta + \\frac{4\\pi}{3}) \\end{vmatrix}$"),
        	           TextMobject("$\\begin{vmatrix} sin(\\theta) & cos(\\theta) & sin(2\\theta) \\\\ sin(\\theta + \\frac{2\\pi}{3}) & cos(\\theta + \\frac{2\\pi}{3}) & sin(2\\theta + \\frac{4\\pi}{3}) \\\\ -sin(\\theta) & -cos(\\theta) & -sin(2\\theta) \\end{vmatrix}$"),
        	           TextMobject("$-\\begin{vmatrix} sin(\\theta) & cos(\\theta) & sin(2\\theta) \\\\ sin(\\theta + \\frac{2\\pi}{3}) & cos(\\theta + \\frac{2\\pi}{3}) & sin(2\\theta + \\frac{4\\pi}{3}) \\\\ sin(\\theta) & cos(\\theta) & sin(2\\theta) \\end{vmatrix}$"),
        	           TextMobject("By using properties of determinants we can say the value is zero."),
        	           TextMobject("Ummm...But let's just apply one more row operation!"),
        	           TextMobject("$\\begin{vmatrix} sin(\\theta) & cos(\\theta) & sin(2\\theta) \\\\ sin(\\theta + \\frac{2\\pi}{3}) & cos(\\theta + \\frac{2\\pi}{3}) & sin(2\\theta + \\frac{4\\pi}{3}) \\\\ -sin(\\theta) & -cos(\\theta) & -sin(2\\theta) \\end{vmatrix}$"),
        	           TextMobject("$\\begin{vmatrix} sin(\\theta)-sin(\\theta) & cos(\\theta)-cos(\\theta) & sin(2\\theta)-sin(2\\theta) \\\\ sin(\\theta + \\frac{2\\pi}{3}) & cos(\\theta + \\frac{2\\pi}{3}) & sin(2\\theta + \\frac{4\\pi}{3}) \\\\ -sin(\\theta) & -cos(\\theta) & -sin(2\\theta) \\end{vmatrix}$"),
        	           TextMobject("$\\begin{vmatrix} 0 & 0 & 0 \\\\ sin(\\theta + \\frac{2\\pi}{3}) & cos(\\theta + \\frac{2\\pi}{3}) & sin(2\\theta + \\frac{4\\pi}{3}) \\\\ -sin(\\theta) & -cos(\\theta) & -sin(2\\theta) \\end{vmatrix}$"),
        	           TextMobject("$\\begin{vmatrix} 0 & 0 & 0 \\\\ sin(\\theta + \\frac{2\\pi}{3}) & cos(\\theta + \\frac{2\\pi}{3}) & sin(2\\theta + \\frac{4\\pi}{3}) \\\\ -sin(\\theta) & -cos(\\theta) & -sin(2\\theta) \\end{vmatrix} = 0$"),
        	           TextMobject("$\\boxed{\\Delta = 0}$")
        	           )
        text1.scale(1.1)
        
        self.play(Transform(text[0],text1[0]))
        self.wait(2)
        text4 = TextMobject("Let's derive some results first!")
        text4.next_to(text,DOWN).set_color(YELLOW)
        self.play(Write(text4))
        self.wait(2)
        self.remove(text4)

        self.play(Transform(text[0],text1[1]))
        #self.wait(1)
        
        text5 = TextMobject("$\\because sin(A+B)+sin(A-B) = 2sin(A)cos(B)$")
        text5.next_to(text,DOWN).set_color(GREEN)
        self.play(Write(text5))
        self.wait(2)
        self.remove(text5)
        

        self.play(Transform(text[0],text1[2]))
        self.wait(1)
        
        self.play(Transform(text[0],text1[3]))
        self.wait(2)
        self.play(Transform(text[0],text1[4]))
        #self.wait(1)
        text6 = TextMobject("$\\because cos(A+B)+cos(A-B) = 2cos(A)cos(B)$")
        text6.next_to(text,DOWN).set_color(GREEN)
        self.play(Write(text6))
        self.wait(2)
        self.remove(text6)


        self.play(Transform(text[0],text1[5]))
        self.wait(1)
       
        self.play(Transform(text[0],text1[6]))
        self.wait(2)

        self.play(Transform(text[0],text1[7]))
        #self.wait(1)
        text7 = TextMobject("$\\because sin(A+B)+sin(A-B) = 2sin(A)cos(B)$")
        text7.next_to(text,DOWN).set_color(GREEN)
        self.play(Write(text7))
        self.wait(2)
        self.remove(text7)

        self.play(Transform(text[0],text1[8]))
        self.wait(1)

        self.play(Transform(text[0],text1[9]))
        self.wait(2)
        text8 = TextMobject("Getting back to the determinant!")
        self.play(Transform(text[0],text8))
        self.wait(2)
        self.play(Transform(text[0],text1[10]))
        self.wait(2)

        
        text2 = TextMobject("$R_{3} \\rightarrow R_{3} + R_{2}$")
        text2.next_to(text,DOWN).set_color(BLUE)
        self.play(Write(text2))
        self.wait(2)
        self.remove(text2)
        
        text1.scale(0.6)
        self.play(Transform(text[0],text1[11]))
        self.wait(2)
        text9 = TextMobject("Notice last row! It's time to apply those derived results.")
        text9.next_to(text,DOWN).set_color(BLUE)
        self.play(Write(text9))
        self.wait(3)
        self.remove(text9)

        text1.scale(1.7)
        self.play(Transform(text[0],text1[12]))
        self.wait(2)
        
        self.play(Transform(text[0],text1[13]))
        self.wait(2)
        text3 = TextMobject("Beautiful! $R_{1}$ and $R_{3}$ are same!")
        text3.next_to(text,DOWN).set_color(BLUE)
        self.play(Write(text3))
        
        self.wait(2)
        self.remove(text3)
        
        text1.scale(0.8)
        self.play(Transform(text[0],text1[14]))
        self.wait(3)
        text1.scale(1.2)
        self.play(Transform(text[0],text1[15]))
        self.wait(3)
        self.play(Transform(text[0],text1[16]))
        self.wait(2)
        text4 = TextMobject("$R_{1} \\rightarrow R_{1} + R_{3}$")
        text4.next_to(text,DOWN).set_color(BLUE)
        self.play(Write(text4))
        self.wait(2)
        self.remove(text4)
        self.play(Transform(text[0],text1[17]))
        self.wait(2)
        self.play(Transform(text[0],text1[18]))
        self.wait(2)
        
        self.play(Transform(text[0],text1[19]))
        self.wait(2)
        text1.scale(2)
        self.play(Transform(text[0],text1[20]))
        self.wait(2)
        #self.play(Transform(text[0],text1[21]))
        self.wait(4)
