from manim import *

class AnimationDemo(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)
        text   = Text("Hello!")

        # 図形を描画しながら表示
        self.play(Create(circle))
        self.wait(1)

        # テキストを手書き風に表示
        self.play(Write(text), run_time=3) # 速さ 通常1(秒)
        self.wait(1)

        # フェードイン
        self.play(FadeOut(circle), FadeOut(text), FadeOut(square)) # 同時に実行される
        self.wait(1)

        # トランスフォーム
        self.play(Transform(circle, square)) # 変形後もオブジェクト名はcircle
        