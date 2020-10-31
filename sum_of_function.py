from manimlib.imports import *
import math
class Fn(Scene):
    def construct(self):
        text = VGroup(
                TextMobject("$F(1)+F(2)+F(3)+\ldots+F(n)=n^{2} F(n) $"),
                TextMobject("Hmm, let's check it for some values!")
            )
        text.arrange(DOWN)\
                .scale(1.5)\
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
        self.wait(2)
        self.remove(text[1])

        text1 = VGroup(
        			   TextMobject("$F(1)+F(2)+F(3)+\ldots+F(n)=n^{2} F(n) $"),
        			   TextMobject("$F(1) = 2006 $"),
        	           TextMobject("$2^{2} F(2) = F(1)+F(2)  $"),
        	           TextMobject("$(2^{2} - 1) F(2) = F(1)  $"),
        	           TextMobject("$F(2) = \\dfrac{F(1)}{2^{2}-1}$"),
        	           TextMobject("$(3^{2}-1)F(3) = F(1) + F(2)$"),
        	           TextMobject("$F(3) = \\dfrac{F(1)}{3^{2}-1} + \\dfrac{F(1)}{(2^{2}-1)\\cdot(3^{2}-1)} $"),
        	           TextMobject("$F(3) = F(1)\\cdot\\bigg[\\dfrac{1}{3^{2}-1} + \\dfrac{1}{(2^{2}-1)\\cdot(3^{2}-1)}\\bigg] $"),
        	           TextMobject("$F(3) = F(1)\\cdot\\bigg[\\dfrac{2^{2}}{(2^{2}-1)\\cdot(3^{2}-1)}\\bigg] $"),
        	           TextMobject("$F(4) = F(1)\\cdot\\bigg[\\dfrac{2^{2}\\cdot 3^{2}}{(2^{2}-1)\\cdot(3^{2}-1) \\cdot (4^{2}-1)}\\bigg] $"),
        	           TextMobject("$F(5) = F(1)\\cdot\\bigg[\\dfrac{2^{2}\\cdot 3^{2}\\cdot4^{2}}{(2^{2}-1)\\cdot(3^{2}-1) \\cdot (4^{2}-1)\\cdot (5^{2}-1)}\\bigg] $"),
        	           TextMobject("$F(5) = F(1)\\cdot\\bigg[\\dfrac{1^{2}\\cdot 2^{2}\\cdot 3^{2}\\cdot4^{2}}{(2-1)(2+1)\\cdot(3-1)(3+1) \\cdot (4-1)(4+1)\\cdot (5-1)(5+1)}\\bigg] $"),
        	           TextMobject("$F(5) = F(1)\\cdot\\bigg[\\dfrac{1^{2}\\cdot 2^{2}\\cdot 3^{2}\\cdot4^{2}}{(1)(3)\\cdot(2)(4) \\cdot (3)(5)\\cdot (4)(6)}\\bigg] $"),
        	           TextMobject("$F(5) = F(1)\\cdot\\bigg[\\dfrac{(1\\cdot 2\\cdot 3\\cdot4)^{2}}{(1\\cdot 2 \\cdot 3 \\cdot 4)(1\\cdot\\frac{2}{2}\\cdot3\\cdot4\\cdot5\\cdot6)}\\bigg] $"),
        	           TextMobject("$F(5) = F(1)\\cdot\\bigg[\\dfrac{(5-1)!}{\\dfrac{(5+1)!}{2}}\\bigg] $"),
        	           TextMobject("$F(5) = F(1)\\cdot\\bigg[\\dfrac{2\\cdot(5-1)!}{(5+1)!}\\bigg] $"),
        	           TextMobject("$F(5) = F(1)\\cdot\\bigg[\\dfrac{2}{5\\cdot(5+1)}\\bigg] $"),
        	           TextMobject("$F(n) = F(1)\\cdot\\bigg[\\dfrac{2}{n\\cdot(n+1)}\\bigg] $"),
        	           TextMobject("$F(n) = 2006\\cdot\\bigg[\\dfrac{2}{n\\cdot(n+1)}\\bigg] $"),
        	           TextMobject("$F(2005) = 2006\\cdot\\bigg[\\dfrac{2}{2005\\cdot(2005+1)}\\bigg] $"),
        	           TextMobject("$\\boxed{F(2005) = \\dfrac{2}{2005}} $")

        	           )
        text1.scale(1.5)

        self.play(Transform(text[0],text1[0]))
        self.wait(2)
        self.play(Transform(text[0],text1[1]))
        self.wait(2)
        self.play(Transform(text[0],text1[2]))
        self.wait(2)
        self.play(Transform(text[0],text1[3]))
        self.wait(2)
        self.play(Transform(text[0],text1[4]))
        self.wait(2)
        self.play(Transform(text[0],text1[5]))
        self.wait(2)
        self.play(Transform(text[0],text1[6]))
        self.wait(2)
        self.play(Transform(text[0],text1[7]))
        self.wait(2)
        self.play(Transform(text[0],text1[8]))
        self.wait(2)
        self.play(Transform(text[0],text1[9]))
        self.wait(2)
        text1.scale(0.7)
        self.play(Transform(text[0],text1[10]))
        self.wait(2)
        text2 = TextMobject("Let's make this one more clean!")
        text2.next_to(text,DOWN)
        self.play(Write(text2))
        self.wait(3)
        text1.scale(0.8)
        self.remove(text2)
        self.play(Transform(text[0],text1[11]))
        self.wait(2)
        
        self.play(Transform(text[0],text1[12]))
        self.wait(2)
        self.play(Transform(text[0],text1[13]))
        self.wait(2)
        self.play(Transform(text[0],text1[14]))
        self.wait(2)
        self.play(Transform(text[0],text1[15]))
        self.wait(2)
        self.play(Transform(text[0],text1[16]))
        self.wait(2)
        text3 = TextMobject("Let's plug in n !")
        text3.next_to(text,DOWN)
        self.play(Write(text3))
        text1.scale(1.5)
        self.wait(2)
        self.remove(text3)
        self.play(Transform(text[0],text1[17]))
        self.wait(3)
        self.play(Transform(text[0],text1[18]))
        #self.add(text2)
        text4 = TextMobject("$\\because F(1) = 2006$")
        text4.next_to(text,DOWN)
        self.add(text4)
        self.wait(2)
        self.remove(text4)
        self.play(Transform(text[0],text1[19]))
        self.wait(2)
        self.play(Transform(text[0],text1[20]))
        self.wait(6)







        


        '''
        text1 = VGroup(
                TextMobject("$F(1)+F(2)+F(3)+\ldots+F(n)=n^{2} F(n) $"),
                TextMobject("Hmm, what can we do?")
            )
        text1.arrange(DOWN)\
                .scale(1.5)\
                .set_fill(opacity=0)

        for position,t in zip([LEFT,RIGHT],text1):
            t_c = t.copy()
            t.next_to(screen,position,buff=0)
            t.set_y(t_c.get_y())

        self.play(ApplyFunction(show_text,text1))
        self.wait(3)
        self.play(ApplyFunction(disappear_text,text1))
        self.wait()    
        '''
