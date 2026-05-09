from manim import *

class StyleDemo(Scene):
    def construct(self):

        # --- 色の指定方法 ---
        c1 = Circle(color=BLUE)
        c2 = Circle(color="#E74C3C")      # 16進数
        c3 = Circle(color=RED)

        VGroup(c1, c2, c3).arrange(RIGHT, buff=0.5)
        self.play(Create(c1), Create(c2), Create(c3))
        self.wait(0.5)

        # --- 塗りつぶし ---
        box = Square(
            color=BLUE,           # 枠線の色
            fill_color=BLUE,      # 塗りつぶし色
            fill_opacity=0.4,     # 透明度（0=透明 / 1=不透明）
        )
        box.move_to(DOWN * 2)
        self.play(Create(box))
        self.wait(0.5)

        # --- アニメーションで色を変える ---
        self.play(box.animate.set_fill(RED, opacity=0.8))
        self.wait(0.5)

        # --- 枠線の太さ ---
        thick = Square(stroke_width=8, color=GREEN)
        thin  = Square(stroke_width=1, color=YELLOW)
        VGroup(thick, thin).arrange(RIGHT, buff=1).move_to(UP * 2)

        self.play(Create(thick), Create(thin))
        self.wait(1)