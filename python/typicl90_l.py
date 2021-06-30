# 競プロ典型90問 012 - Red Painting
# https://atcoder.jp/contests/typical90/tasks/typical90_l
# tag: グリッド 経路 Union_Find 

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

    # xの所属するグループのメンバー数を返す
    def get_member_count(self, x):
        x = self.find(x)
        return -self.parent[x]

    # xの所属するグループのメンバーをリストで返す
    def get_group_members(self, x):
        x = self.find(x)
        return [i for i in range(self.N) if self.find(i) == x]

    # 全ての{リーダー:グループメンバー数}を辞書形式で返す
    def get_all_member_count(self):
        return {idx:-n for idx, n in enumerate(self.parent) if n < 0}

    # 全ての{リーダー:[メンバー一覧]}を辞書形式で返す
    # もしもこれが欲しいだけなら、グラフ探索するほうが速いんじゃないかな……
    def get_all_group_members(self):
        agm_dic = {}
        for i in range(self.N):
            agm_dic.setdefault(self.find(i), [])
            agm_dic[self.find(i)].append(i)
        return agm_dic


def main():
    H, W = map(int, input().split())
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]

    field = [[False] * W for _ in range(H)]
    uft = Union_Find(H*W)

    for q in queries:
        if q[0] == 1:
            op, r, c = q
            pos = W*(r-1) + (c-1)
            field[r-1][c-1] = True
            for tr, tc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= tr-1 < H and 0 <= tc-1 < W and field[tr-1][tc-1]:
                    uft.unite(pos, W*(tr-1)+(tc-1))
        
        else:
            op, r1, c1, r2, c2 = q
            if field[r1-1][c1-1] and field[r2-1][c2-1] and uft.samep(W*(r1-1)+(c1-1), W*(r2-1)+(c2-1)):
                print('Yes')
            else:
                print('No')

main()
