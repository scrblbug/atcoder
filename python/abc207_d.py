# AtCoder Begv1 Contest 207 D - Congruence Points
# https://atcoder.jp/contests/abc207/tasks/abc207_d
# tag: 計算幾何 点集合 回転 一致 コーナーケース 複素平面

# どちらも 0 でない二つのベクトル V(p, q) U(r, s) があり、
# これを複素平面上に取ったときを考える。
# V, U の関係は V / U にて記述することが可能で、
# p + qi / r + si =
# (p + qi)(r - si) / r^2 + s^2 =
# (pr + qs) - (ps - qr)i / r^2 + s^2
# つまり、r^2 + s^2 が固定されているなら、
# pr + qs, ps - qr を用いて回転後の U に対するV の
# 一致判定が出来る。

# これをふまえて……

# 点集合を、setA と setB とする。
# setA から適当に 2 点を選ぶ。これを o, a とする。
# この o->a を基準ベクトルと仮定する。
# setA に含まれる、o, a を除く全ての点（仮に b とする）の、
# o->a と o->b の関係を、上記式から導いておく。

# setB から全ての 2 点の組み合わせを選び、同様の操作を行い、
# 一致するかどうかを確認する。

from itertools import combinations
def main():
    N = int(input())
    set_a = [list(map(int, input().split())) for _ in range(N)]
    set_b = [list(map(int, input().split())) for _ in range(N)]

    # コーナーケース
    if N == 1:
        print('Yes')
        return

    # 点集合 pset から、原点と第一点を指定した際に、
    # 他の点の相対的な位置を示すリストを得る関数を作成。
    def get_relations(pset, idx_o, idx_a):
        xo, yo = pset[idx_o]
        xa, ya = pset[idx_a]
        p, q = xa - xo, ya - yo

        value_list = []

        for xb, yb in pset:
            if (xb, yb) == (xo, yo) or (xb, yb) == (xa, ya):
                continue
            r, s = xb - xo, yb - yo
            v1 = p*r + q*s
            v2 = p*s - q*r
            value_list.append((v1, v2))
        
        return(sorted(value_list))

    # 適当な 2点から、set_a の情報を生成しておく
    xo, yo = set_a[0]
    xa, ya = set_a[1]
    base_dist = (xa - xo)**2 + (ya - yo)**2
    target = get_relations(set_a, 0, 1)

    for i in range(N):
        for j in range(N):
            xo, yo = set_b[i]
            xa, ya = set_b[j]

            # そもそも基準にする 2点の距離が違っていたらスキップ
            if (xa - xo)**2 + (ya - yo) ** 2 != base_dist:
                continue
            
            # set_b[i], set_b[j] を基準とする情報を生成
            test = get_relations(set_b, i, j)

            # 一致するかどうかを判定
            if test == target:
                print('Yes')
                return
    else:
        print('No')

main()
