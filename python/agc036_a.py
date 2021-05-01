# AtCoder Grand Contest 036 A - Triangle
# https://atcoder.jp/contests/agc036/tasks/agc036_a
# tag: 計算幾何

# 二次元平面上において、ベクトル v1:(a, b), v2:(c, d)の
# v1 x v2: (ad - bc) （スカラー値だが外積と呼ぶこともあるらしい）は、
# ベクトル v1 v2 を隣り合う二辺に取る平行四辺形の向き付き面積に等しい。

# ……要するに、平面上に (0, 0), (a, b), (c, d) の3つの点がある時、
# この3つの点による三角形の面積は、|ad - bc| / 2 になる。

# ここでは、わざわざ三角形の面積が S/2 となる、とされているので、
# 要するに ad - bc = S となる a, b, c, d をみつければいい。

def main():
    S = int(input())

    # ad - bc を任意の数 (=S) にしたいので、とりあえず
    a = 10**9
    b = 1
    # としてやれば、10**9 * d - c と簡単にできる

    # S/a を切り上げたものが d
    d = ((S-1) // a) + 1

    c = 10**9 * d - S

    print(0, 0, a, b, c, d)

main()
