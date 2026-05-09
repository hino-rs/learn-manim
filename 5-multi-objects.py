from manim import *

class VGroupDemo(Scene):
    def construct(self):

        # --- VGroup：複数オブジェクトをひとまとめ ---
        circle = Circle(color=BLUE)
        label  = Text("circle", font_size=28)

        # labelをcircleの下に配置
        label.next_to(circle, DOWN)

        # グループ化
        group = VGroup(circle, label)

        self.play(Create(group))
        self.wait(0.5)

        # グループごと動かせる
        self.play(group.animate.shift(LEFT * 2))
        self.wait(0.5)

        # --- 位置関係メソッドの比較 ---
        box1 = Square(color=RED)
        box2 = Square(color=GREEN)
        box3 = Square(color=YELLOW)

        box1.move_to(ORIGIN)
        box2.next_to(box1, RIGHT, buff=0.5)   # box1の右に0.5の余白
        box3.next_to(box1, LEFT,  buff=0.5)   # box1の左に0.5の余白

        self.play(Create(box1), Create(box2), Create(box3))
        self.wait(0.5)

        # VGroupでまとめて整列
        row = VGroup(box1, box2, box3)
        self.play(row.animate.shift(RIGHT * 2 + UP * 2))
        self.wait(1)

"""
group = VGroup(objA, objB, objC)

# まとめて操作できる
self.play(group.animate.shift(UP))
self.play(FadeOut(group))

# インデックスでアクセスも可能
group[0]  # objA
group[1]  # objB
"""