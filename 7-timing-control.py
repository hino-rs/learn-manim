from manim import *

class TimingDemo(Scene):
    def construct(self):

        box_list = [
            Square(color=BLUE, fill_color=BLUE, fill_opacity=0.3)
            for _ in range(4)
        ]
        VGroup(*box_list).arrange(RIGHT, buff=0.5)

        # --- run_time：1つのアニメの長さ ---
        self.play(Create(box_list[0]), run_time=2.0)   # ゆっくり
        self.play(Create(box_list[1]), run_time=0.5)   # 速く
        self.wait(0.5)

        # --- rate_func：動きのイージング ---
        self.play(
            box_list[0].animate.shift(UP),
            rate_func=linear,           # 一定速度
        )
        self.play(
            box_list[1].animate.shift(UP),
            rate_func=smooth, # 加速→減速（自然な動き）
        )
        self.wait(0.5)

        # --- lag_ratio：グループ内の時間差 ---
        self.play(
            Create(box_list[2]),
            Create(box_list[3]),
            lag_ratio=0.0,   # 同時
        )
        self.wait(0.5)

        self.play(
            FadeOut(box_list[2]),
            FadeOut(box_list[3]),
            lag_ratio=0.5,   # 時間差あり（ドミノ的に）
        )
        self.wait(1)