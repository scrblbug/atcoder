# AtCoder Regular Contest 042 B - アリの高橋くん
# https://atcoder.jp/contests/arc042/tasks/arc042_b
# tag: 計算幾何 基礎問題 高橋君

# 高橋くんの座標を T とする。
# 対象の多角形のすべての辺と T との最短距離のうち、
# もっとも短いものが答えになる。

# T.
#A----B

# の位置関係の時はいいとして、

# T.
#    A----B

# の時は大丈夫？となるが、この場合は T がはみ出ている側の
# 隣の辺と T との距離のほうが短くなるので、回答には
# 影響しない。

# T と AB との距離については、
# A を原点に重なるように全ての点を平行移動しておく。
# このときに AB と AT をそれぞれベクトル
# AB(a, b), AT(p, q) として複素平面上に取ると、
# 求めるものは AT / AB * |AB| の y 成分の絶対値となる。
# これは、AB の持つ角度だけ AT を逆に回転してやれば、
# T と AB との距離は T と x 座標との距離になるということ。

# 具体的には、
# (p + qi) / (a + bi) * |AB| =
# (p + qi)(a - bi) / (a + bi)(a - bi) * |AB| =
# ((ap + bq) + (aq - bp)i) / (a^2 + b^2) * |AB|

# より、求めるものは、
# (aq - bp) / (a^2 + b^2) * sqrt(a^2 + b^2)

# 以上を踏まえて……

def main():
    x, y = map(int, input().split())
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]

    result = 10**10

    for i in range(N):
        j = (i + 1) % N

        # 点 A, B を取得
        ax, ay = points[i]
        bx, by = points[j]

        a, b = bx - ax, by - ay
        p, q = x - ax, y - ay

        # 上記考察より、AB と T との距離を求める
        dist = abs((a*q - b*p) / (a**2 + b**2) * (a**2 + b**2)**0.5)

        if result > dist:
            result = dist

    print(result)

main()