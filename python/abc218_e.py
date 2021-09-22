# AtCoder Beginner Contest 218 E - Destruction
# https://atcoder.jp/contests/abc218/tasks/abc218_e
# tag: グラフ 木 最小全域木 クラスカル法 Union_Find

# グラフ上から辺を取り除きつつ、その都度連結判定を行うのは難しい。
# そこで、逆に点数が少ない辺を用いて全ての頂点を繋げることを考える。

# つまり、最初は頂点のみがある状態からスタートし、点数が
# 低い辺を順番に用いて徐々にグラフを連結していく。
# 全ての頂点が連結された時、使用しなかった辺を報酬に
# 変換できる……といった感じになる。

# この時、注意事項が 2つある。
# 一つは、点数が負の辺は必ず用いることにするということ。
# もう一つは、点数が正で、かつ用いる必要がない辺、
# つまり既に連結済みの頂点同士を結ぶ辺は使用しない、とすること。

# 頂点同士が連結かどうかに関しては、Union_Findを用いて
# 管理を行うと実装しやすい。

# ちなみに、この条件から点数が負の辺を用いる～という条件を
# なくせば、クラスカル法と呼ばれる最小全域木の構成方法となる。

# Union_Find クラス
class Union_Find:
    # 親管理リストと高さ管理リストを初期化し、
    # 要素N個のUnion-Find森を作成する。
    # 親管理リストは、基本的には自分のひとつ上の親を表すが、
    # 値が負の場合には、自身が最上位の親(リーダー)であることを表し、
    # 自分を含めたグループの人数を管理することとする
    def __init__(self, N):
        self.parent = [-1] * N
        self.rank = [0] * N
        self.group_count = N
        self.N = N

    # xの所属するグループのリーダーを返す
    def find(self, x):
        # 自分自身がリーダーなら、自分を返す
        if self.parent[x] < 0:
            return x

        # 再帰的に捜索し、見つかれば繋ぎ変えておく
        # (計算量が増える＝面倒くさいので)高さ管理は行わない
        par = self.find(self.parent[x])
        self.parent[x] = par
        return par

    # xとyのグループを統合する
    def unite(self, x, y):
        # それぞれのリーダーに対する操作を行うことになる
        x = self.find(x)
        y = self.find(y)

        # リーダーが同じなら何もする必要がない
        if x == y:
            return (-1, -1)

        # 木の高さが同じ場合：
        # グループの人数を合計しつつ適当に繋ぎ、繋げられた方の高さを1増やす
        if self.rank[x] == self.rank[y]:
            self.parent[x] += self.parent[y]
            self.parent[y] = x
            self.rank[x] += 1
            self.group_count -= 1
            return (x, y)

        # 木の高さが違うなら、低い方を高い方につなぐ
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.group_count -= 1
        return (x, y)

    # xとyが同じグループかどうかを調べる
    def samep(self, x, y):
        return self.find(x) == self.find(y)

# ここからメイン。
def main():
    N, M = map(int, input().split())
    path_dat = [list(map(int, input().split())) for _ in range(M)]

    # 点数をもとに辺をソートしておく。
    path_dat.sort(key=lambda x: x[2])

    uft = Union_Find(N)

    result = 0

    for a, b, c in path_dat:
        a -= 1
        b -= 1

        # まだ連結でない頂点を結ぶ or 点数が負なら、
        # 辺を使用する（＝残す）。
        if uft.find(a) != uft.find(b) or c < 0:
            uft.unite(a, b)

        # でなければ、辺を使用しない（＝取り除く）
        else:
            result += c

    print(result)

main()
