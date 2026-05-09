# 位置関係

## 位置関係メソッド

|メソッド|意味|
|---|---|
|`A.next_to(B, DIR, buff=0.5)`|BのDIR方向に配置（余白 buff）|
|`A.move_to(B)`|Bの中心に移動|
|`A.align_to(B, DIR)`|BのDIR端に揃える|
|`A.get_center()`|Aの中心座標を取得|
|`A.get_top()`|Aの上端座標を取得|
|`A.get_bottom()`|Aの下端座標を取得|

## buffで間隔調整

```python
label.next_to(block, DOWN, buff=0.1)  # ぴったり寄せたい
label.next_to(block, DOWN, buff=0.5)  # 少し離したい
```

デフォルトは`buff=0.25`
