from manim import *

class iudq(Scene):
    def construct(self):
        loveletter = Tex(
            "All I want is to be with you forever"
        ).scale(1)
        iudq = Tex(
            "Iu be DQ cua tui"
        ).scale(0.001)
        self.play(Write(loveletter))
        graph = ImplicitFunction(
            lambda x, y: (x ** 2 + y ** 2 - 1) ** 3 - x ** 2 * y ** 3, 
            color = RED
        ).scale(5)
        animations = [
            FadeOut(loveletter),
            FadeIn(iudq),
        ]
        self.play(Create(graph))
        self.play(graph.animate.scale(0.001), loveletter.animate.scale(0.001), run_time = 2)
        self.play(AnimationGroup(*animations), run_time = 0.01)
        self.play(graph.animate.scale(680), iudq.animate.scale(1200), run_time = 2)
        self.wait()
        
        