# AtCoder Beginner Contest 197 D - Opposite
# https://atcoder.jp/contests/abc197/tasks/abc197_d
# tag: 計算幾何 回転 基礎問題

# 数学力が低いと解くのが厳しく見えるが、実は計算幾何では
# かなり基礎的な問題とも言える。

# 公式解説では atan2 を利用して解いているが、
# ここではベクトルと回転行列を使用した。

import math
def main():
    N = int(input())
    x0, y0 = list(map(int, input().split()))
    xh, yh = list(map(int, input().split()))

    # 中心点を求める
    xc, yc = (x0 + xh) / 2, (y0 + yh) / 2

    # 中心点 → (x0, y0) へのベクトルを出しておく
    vx, vy = x0 - xc, y0 - yc

    # 回転角を出す
    rotate = math.pi * 2 / N

    # ベクトルを回転させる
    vx_rotated = vx * math.cos(rotate) - vy * math.sin(rotate)
    vy_rotated = vx * math.sin(rotate) + vy * math.cos(rotate)

    # 答えの点を求める
    x_ans = xc + vx_rotated
    y_ans = yc + vy_rotated

    print(x_ans, y_ans)

main()
