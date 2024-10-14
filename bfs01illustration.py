from manim import *
from manim.mobject.graph import Graph
import networkx as nx

class GraphManualPosition(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6]
        edges = [(1, 2), (1, 3), (2, 3), (3, 4), (2, 4), (3, 5), (4, 5), (4, 6), (5, 6)]
        lt = {1 : [-4.8, 3, 0], 2: [-6, 1.5, 0], 3: [-3.6, 1.5, 0], 4: [-6, 0, 0], 5: [-3.6, 0, 0], 6: [-4.8, -1.5, 0]}
        authorities = Text("Made by Vbee", color=TEAL, font_size= 18).to_edge(DR)
        self.add(authorities)
        G = Graph(vertices, edges, layout=lt, labels = True)
        dist_table = Table(
            [["u", "1", "2", "3", "4", "5", "6"], ["d[u]", " ", " ", " ", " ", " ", " "]]
        ).scale(0.5).shift(UR * 2)
        
        dist1 = Tex(r"$0$").shift(RIGHT * 0.6).shift(UP * 1.6)
        dist2 = Tex(r"$\infty$").shift(RIGHT * 1.41).shift(UP * 1.6)
        dist3 = Tex(r"$\infty$").shift(RIGHT * 2.22).shift(UP * 1.6)
        dist4 = Tex(r"$\infty$").shift(RIGHT * 3.03).shift(UP * 1.6)
        dist5 = Tex(r"$\infty$").shift(RIGHT * 3.84).shift(UP * 1.6)
        dist6 = Tex(r"$\infty$").shift(RIGHT * 4.65).shift(UP * 1.6)
        weight1 = Tex("$1$", font_size = 33).shift(LEFT * 5.7).shift(UP * 2.5)
        weight2 = Tex("$0$", font_size = 33).shift(LEFT * 3.95).shift(UP * 2.5)
        weight3 = Tex("$0$", font_size = 33).shift(LEFT * 4.8).shift(UP * 1.82)
        weight4 = Tex("$1$", font_size = 33).shift(LEFT * 6.3).shift(UP * 0.82)
        weight5 = Tex("$1$", font_size = 33).shift(LEFT * 5).shift(UP * 0.95)
        weight6 = Tex("$1$", font_size = 33).shift(LEFT * 3.3).shift(UP * 0.8)
        weight7 = Tex("$0$", font_size = 33).shift(LEFT * 4.8).shift(DOWN * 0.3)
        weight8 = Tex("$0$", font_size = 33).shift(LEFT * 5.7).shift(DOWN * 0.9)
        weight9 = Tex("$1$", font_size = 33).shift(LEFT * 3.95).shift(DOWN * 0.9)
        deque = Text("Deque", color=RED, font_size=30).shift(LEFT*1)

        weight_group = VGroup(
            weight1, weight2, weight3, weight4, weight5, weight6, weight7, weight8, weight9
        )
        dist_group = VGroup(
            dist1, dist2, dist3, dist4, dist5, dist6
        )
        self.add(G)
        self.add(weight_group)
        self.add(dist_table)
        self.add(dist_group)
        self.add(deque)
        index1 = Tex(r"$1$", color=BLACK).move_to(G.vertices[1])
        index2 = Tex(r"$2$", color=BLACK).move_to(G.vertices[2])
        index3 = Tex(r"$3$", color=BLACK).move_to(G.vertices[3])
        index4 = Tex(r"$4$", color=BLACK).move_to(G.vertices[4])
        index5 = Tex(r"$5$", color=BLACK).move_to(G.vertices[5])
        index6 = Tex(r"$6$", color=BLACK).move_to(G.vertices[6])
        allindex = VGroup(
            index1, index2, index3, index4, index5, index6
        )
        self.add(allindex)
        
        currentNode = Text("Current Node", color = RED, font_size = 30).shift(DL * 2)
        currentNode.shift(RIGHT * 0.4)
        self.add(currentNode)
        Node1 = LabeledDot(Tex(r"$1$"), color = BLUE_E, radius = 0.3, fill_opacity = 0.8).shift(RIGHT * 0.2)
        self.add(Node1)
        BuddyNode = LabeledDot(Tex(""), color = BLUE_E, radius = 0.3, fill_opacity = 0).next_to(deque)
        BuddyNodeShow = LabeledDot(Tex(""), radius = 0.3, fill_opacity=0).shift(DR * 1)
        self.wait()

        self.play(Node1.animate.shift(DOWN * 2), run_time = 1)
        G.vertices[1].fill_color=TEAL
        self.play(G.vertices[1].animate)
        
        G.vertices[2].fill_color = YELLOW
        Node2 = LabeledDot(Tex(r"$2$"), color = BLUE_E, radius = 0.3, fill_opacity = 0.8).next_to(BuddyNodeShow)
        self.play(G.vertices[2].animate, Create(Node2), run_time = 1)
        newdist2 = Tex(r"$1$").shift(RIGHT * 1.41).shift(UP * 1.6)
        self.play(ReplacementTransform(dist2, newdist2), run_time = 1)
        self.play(Node2.animate.next_to(deque), run_time = 1)
        G.vertices[2].fill_color = WHITE
        self.play(G.vertices[2].animate)

        G.vertices[3].fill_color = YELLOW
        Node3 = LabeledDot(Tex(r"$3$"), color = BLUE_E, radius = 0.3, fill_opacity = 0.8).next_to(BuddyNodeShow)
        self.play(G.vertices[3].animate, Create(Node3), run_time = 1)
        newdist3 = Tex(r"$0$").shift(RIGHT * 2.22).shift(UP * 1.6)
        self.play(ReplacementTransform(dist3, newdist3), run_time = 1)
        self.play(Node2.animate.next_to(BuddyNode))
        self.play(Node3.animate.next_to(Node2, LEFT), run_time = 1)
        G.vertices[3].fill_color = WHITE
        self.play(G.vertices[3].animate)

        G.vertices[1].fill_color=GREY
        animationtemp = (
            FadeOut(Node1),
        )
        self.play(AnimationGroup(*animationtemp))
        self.play(G.vertices[1].animate)

        self.play(Node3.animate.shift(DOWN * 2), Node2.animate.next_to(deque), run_time = 1)
        G.vertices[3].fill_color=TEAL
        self.play(G.vertices[3].animate)

        G.vertices[2].fill_color = YELLOW
        Node21 = LabeledDot(Tex(r"$2$"), color = BLUE_E, radius = 0.3, fill_opacity = 0.8).next_to(BuddyNodeShow)
        self.play(G.vertices[2].animate, Create(Node21), run_time = 1)
        newdist21 = Tex(r"$0$").shift(RIGHT * 1.41).shift(UP * 1.6)
        self.play(ReplacementTransform(newdist2, newdist21), run_time = 1)
        self.play(Node2.animate.next_to(BuddyNode), Node21.animate.next_to(deque), run_time = 1)
        G.vertices[2].fill_color = WHITE
        self.play(G.vertices[2].animate)

        G.vertices[4].fill_color = YELLOW
        Node4 = LabeledDot(Tex(r"$4$"), color = BLUE_E, radius =  0.3, fill_opacity = 0.8).next_to(BuddyNodeShow)
        self.play(G.vertices[4].animate, Create(Node4), run_time = 1)
        newdist4 = Tex(r"$1$").shift(RIGHT * 3.03).shift(UP * 1.6)
        self.play(ReplacementTransform(dist4, newdist4), run_time = 1)
        self.play(Node4.animate.next_to(Node2), run_time = 1)
        G.vertices[4].fill_color = WHITE
        self.play(G.vertices[4].animate)

        G.vertices[5].fill_color = YELLOW
        Node5 = LabeledDot(Tex(r"$5$"), color = BLUE_E, radius =  0.3, fill_opacity = 0.8).next_to(BuddyNodeShow)
        self.play(G.vertices[5].animate, Create(Node5), run_time = 1)
        newdist5 = Tex(r"$1$").shift(RIGHT * 3.84).shift(UP * 1.6)
        self.play(ReplacementTransform(dist5, newdist5), run_time = 1)
        self.play(Node5.animate.next_to(Node4), run_time = 1)
        G.vertices[5].fill_color = WHITE
        self.play(G.vertices[5].animate)

        G.vertices[3].fill_color=GREY
        animationtemp2 = (
            FadeOut(Node3),
        )
        self.play(AnimationGroup(*animationtemp2), G.vertices[3].animate)
        # self.play(G.vertices[3].animate)
        
        self.play(Node21.animate.shift(DOWN * 2), Node2.animate.next_to(deque), Node4.animate.next_to(BuddyNode), Node5.animate.next_to(Node2), run_time = 1)
        G.vertices[2].fill_color=TEAL
        self.play(G.vertices[2].animate)

        G.vertices[4].fill_color = YELLOW
        Node41 = LabeledDot(Tex(r"$4$"), color = BLUE_E, radius =  0.3, fill_opacity = 0.8).next_to(BuddyNodeShow)
        self.play(G.vertices[4].animate, Create(Node41), run_time = 1)
        animationtemp3 = (
            FadeOut(Node41),
        )
        self.play(AnimationGroup(*animationtemp3))
        # self.remove(Node41)
        G.vertices[4].fill_color = WHITE
        self.play(G.vertices[4].animate)

        G.vertices[2].fill_color=GREY
        animationtemp4 = (
            FadeOut(Node21),
        )
        self.play(AnimationGroup(*animationtemp4), G.vertices[2].animate)
        # self.remove(Node21)
        # self.play(G.vertices[2].animate)

        self.play(Node2.animate.shift(DOWN * 2), Node4.animate.next_to(deque), Node5.animate.next_to(Node2), run_time = 1)
        animationtemp5 = (
            FadeOut(Node2),
        )
        self.play(AnimationGroup(*animationtemp5))
        # self.remove(Node2)

        self.play(Node4.animate.shift(DOWN * 2), Node5.animate.next_to(deque), run_time = 1)
        G.vertices[4].fill_color=TEAL
        self.play(G.vertices[4].animate)

        G.vertices[5].fill_color = YELLOW
        Node51 = LabeledDot(Tex(r"$5$"), color = BLUE_E, radius =  0.3, fill_opacity = 0.8).next_to(BuddyNodeShow)
        self.play(G.vertices[5].animate, Create(Node51), run_time = 1)
        animationtemp6 = (
            FadeOut(Node51),
        )
        self.play(AnimationGroup(*animationtemp6))
        # self.remove(Node51)
        G.vertices[5].fill_color = WHITE
        self.play(G.vertices[5].animate)

        G.vertices[6].fill_color = YELLOW
        Node6 = LabeledDot(Tex(r"$6$"), color = BLUE_E, radius =  0.3, fill_opacity = 0.8).next_to(BuddyNodeShow)
        self.play(G.vertices[6].animate, Create(Node6), run_time = 1)
        newdist6 = Tex(r"$1$").shift(RIGHT * 4.65).shift(UP * 1.6)
        self.play(ReplacementTransform(dist6, newdist6), run_time = 1)
        self.play(Node5.animate.next_to(BuddyNode), Node6.animate.next_to(deque), run_time = 1)
        G.vertices[6].fill_color = WHITE
        self.play(G.vertices[6].animate)

        G.vertices[4].fill_color=GREY
        animationtemp7 = (
            FadeOut(Node4),
        )
        self.play(AnimationGroup(*animationtemp7))
        # self.remove(Node4)
        self.play(G.vertices[4].animate)

        self.play(Node6.animate.shift(DOWN * 2), Node5.animate.next_to(deque), run_time = 1)
        G.vertices[6].fill_color=TEAL
        self.play(G.vertices[6].animate)

        G.vertices[5].fill_color = YELLOW
        Node51 = LabeledDot(Tex(r"$5$"), color = BLUE_E, radius =  0.3, fill_opacity = 0.8).next_to(BuddyNodeShow)
        self.play(G.vertices[5].animate, Create(Node51), run_time = 1)
        animationtemp8 = (
            FadeOut(Node51),
        )
        self.play(AnimationGroup(*animationtemp8))
        # self.remove(Node51)
        G.vertices[5].fill_color = WHITE
        self.play(G.vertices[5].animate)

        G.vertices[6].fill_color=GREY
        animationtemp9 = (
            FadeOut(Node6),
        )
        self.play(AnimationGroup(*animationtemp9))
        # self.remove(Node6)
        self.play(G.vertices[6].animate)

        self.play(Node5.animate.shift(DOWN * 2), run_time = 1)
        G.vertices[5].fill_color=TEAL
        self.play(G.vertices[5].animate)

        G.vertices[5].fill_color=GREY
        animationtemp10 = (
            FadeOut(Node5),
        )
        self.play(AnimationGroup(*animationtemp10))
        # self.remove(Node5)
        self.play(G.vertices[5].animate)
        self.wait()