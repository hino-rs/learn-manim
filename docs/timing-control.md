# タイミング制御

## rate_func

```plaintext
linear          # 一定速度
smooth          # 加速→減速（デフォルト・ease_in_out相当）
rush_into       # 加速して止まる
rush_from       # 速い状態からゆっくり止まる
there_and_back  # 行って戻る
double_smooth   # smoothを2回かけたようなより滑らかな動き
lingering       # ゆっくり始まってゆっくり終わる
```

## lag_ratio

```python
# 0.0 = 完全同時
# 0.5 = 前のアニメが半分終わったら次が始まる
# 1.0 = 完全に順番（前が終わってから次）

self.play(
    AnimationGroup(
        FadeIn(box1),
        FadeIn(box2),
        FadeIn(box3),
        lag_ratio=0.3
    )
)
```
