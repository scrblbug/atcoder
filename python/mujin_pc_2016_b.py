# MUJIN プログラミングチャレンジ B - ロボットアーム
# https://atcoder.jp/contests/mujin-pc-2016/tasks/mujin_pc_2016_b
# tag: 計算幾何

# 原点から一番離れる最大の範囲は、OA + AB + BC で問題無い。
# 最小がどうなるのかを考える。

# 原点を通ることが出来る ＝ 最小距離を 0 にできるのは、
# OA, AB, BC で三角形をつくれるとき。
# この必要十分条件は、この3つの辺の長さを短い順に
# x, y, z としたとき、x + y >= z であること。

# また、逆に三角形を作れない場合、つまり x + y < z の時は、
# 原点に対して z - (x + y) の距離までしか近づくことが
# できないことになる。

import math
def main():
    l = list(map(int, input().split()))

    # 最長辺と、それ以外の辺の合計を出しておく
    mx = max(l)
    rest = sum(l) - mx

    result = math.pi * sum(l)**2

    # 原点を通れない場合は、内側の円の面積を引く
    if rest < mx:
        result -= math.pi * (mx - rest)**2
    
    print(result)

main()
