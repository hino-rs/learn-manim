from manim import *

class TextDemo(Scene):
    def construct(self):
        # 普通のテキスト
        t1 = Text("Hello, Manim!", font_size=72)
        # t1 = Text("パイソン", font="BIZ UDGothic") # 日本語を使うときはフォント明示

        # 数式・記号 (LaTeX記法)
        t2 = MathTex(r"E = mc^2") # rawstringにする

        self.add(t1, t2)
        self.wait(2)

# 文章 + 数式混在:
# Tex(r"...)