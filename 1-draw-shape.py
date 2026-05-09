from manim import *

class ShapeDemo(Scene):
    def construct(self):
        circle = Circle(radius=1.5, color=BLUE)
        square = Square(side_length=2, color=RED)
        rect   = Rectangle(width=3, height=1.5, color=GREEN)

        # 即座に画面に置く (アニメーションなし)
        self.add(circle, square, rect) 

        # アニメーションとして表示する
        self.wait(2)
