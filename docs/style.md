# スタイル

## 組み込みカラー定数

```python
# 基本色
RED, BLUE, GREEN, YELLOW, WHITE, BLACK, GRAY

# 明暗バリエーション
BLUE_A   # 一番薄い
BLUE_B
BLUE_C   # ← これが BLUE と同じ
BLUE_D
BLUE_E   # 一番濃い

# その他便利なもの
ORANGE, PURPLE, TEAL, PINK, GOLD
```

## `fill_opacity`

```python
# メモリブロックらしい見た目はこれ
block = Rectangle(
    width=2.5, height=1,
    color=BLUE,
    fill_color=BLUE,
    fill_opacity=0.3,   # 薄く塗って中が見える感じに
    stroke_width=2,
)
```

`fill_opacity=0` だと枠線だけ、`1` だと完全に塗りつぶし。

## `arrange()`

```python
group = VGroup(box1, box2, box3)

group.arrange(RIGHT, buff=0.5)   # 横並び
group.arrange(DOWN,  buff=0.3)   # 縦並び
```

`next_to()` を何度も書かなくて済むので、複数ブロックを並べるときに重宝します。
