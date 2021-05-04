# AtCoder Grand Contest 018 A - Getting Difference
# https://atcoder.jp/contests/agc018/tasks/agc018_a
# tag: 整数 公約数 考察

# 数が多すぎるとよくわからなくなるので、
# 2 つだけの時を考えてみる。

# (11, 8) の時
# 11-8=3, 8-3=5, 5-3=2, 3-2=1
# 1 ができれば、11 以下の数は全て作れる。

# (10, 6) の時
# 10-6=4, 6-4=2, 10-2=8
# (2, 4, 6, 8, 10) を作成可能。

# 実のところ、行う操作はユークリッドの互除法そのもの。
# a, b の二種類しか数がない場合は、gcd(a, b) の
# 倍数を作成可能。ただし、最大値は max(a, b)

# となると、ボールが 2 個以上の場合でも、
# 他のボールと同様の操作を繰り返すと、
# 全てのボールの数字の最大公約数を作成可能。

# すると、一番大きなボールからその最大公約数を
# 順次引いていくことができ、結局、上記と同じように
# 最大公約数の倍数（上限はボールの最大値）を
# 作成可能となる。

from math import gcd
from functools import reduce
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 全ての数字の最大公約数を求める。
    # reduce を使わない時は
    # g = A[0]
    # for a in A[1:]:
    #     g = gcd(g, a)
    # みたいな感じ
    g = reduce(gcd, A)

    # 最大値
    mx = max(A)

    # 上記の考察の通り
    if K <= mx and K % g == 0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')

main()
