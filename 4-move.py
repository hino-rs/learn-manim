from manim import *

class MoveDemo(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.wait(0.5)

        # shift: 今の位置から相対移動
        # .playの中に.animate
        self.play(circle.animate.shift(RIGHT * 2)) # または[2, 0, 0]
        self.wait(0.5)

        # 複数のプロパティを同時に変える
        self.play(
            circle.animate.move_to(LEFT * 2).scale(0.5).set_color(YELLOW)
        )
        self.wait(0.5)

        # 2つを同時に動かす
        self.add(square)
        self.play(
            circle.animate.shift(DOWN * 2),
            square.animate.shift(UP * 2),
        )
        self.wait(1)