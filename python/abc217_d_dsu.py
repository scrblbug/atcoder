# クエリを逆から見ていった場合、バラバラになっている木を
# どんどんくっつけていくという操作になる。
# これを Union Find で管理しつつ、順次（逆から）答えを
# 求めていくことが可能。

from typing import Union


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
    # (xのリーダー（統合先), yのリーダー（統合元）) を返す
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

    # xの所属するグループのメンバー数を返す
    def get_member_count(self, x):
        x = self.find(x)
        return -self.parent[x]

# ここからメイン
def main():
    L, Q = map(int, input().split())
    queries = [list(map(int, input().split())) for _ in range(Q)]

    # あらかじめ出てくる地点を先読みする。
    # 0, L も切られる地点として含めておく。
    points = list(set([x for c, x in queries] + [0, L]))
    points.sort()

    # 各部分の長さ。
    piece_length = [r - l for l, r in zip(points, points[1:])]

    # クエリ上の位置 → n 番目の座標圧縮用辞書
    pos_to_n = {pos: n for n, pos in enumerate(points)}

    # Union_Find木の作成。
    # 各要素は最終状態での各ピースとする。
    # 結合時はリーダーを元にして piece_length を更新する。
    uft = Union_Find(len(piece_length))

    # 実際に切られる地点。
    cut_points = set([x for c, x in queries if c == 1] + [0, L])

    # 切られない地点は、あらかじめ結合しておく。
    for p in points:
        if p not in cut_points:
            x, y = uft.unite(pos_to_n[p]-1, pos_to_n[p])
            piece_length[x] += piece_length[y]

    result = []
    # 逆順にクエリを処理していく。
    for c, x in queries[::-1]:
        # 切るクエリなら、逆に木を結合する。
        if c == 1:
            x, y = uft.unite(pos_to_n[x]-1, pos_to_n[x])
            piece_length[x] += piece_length[y]

        # 指示された地点の長さを返す。
        else:
            result.append(piece_length[uft.find(pos_to_n[x])])

    # 得られた答えを逆順に出力。
    for r in result[::-1]:
        print(r)

main()
