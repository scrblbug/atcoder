# AtCoder Beginners Contest 090 D - People on a Line
# https://atcoder.jp/contests/abc087/tasks/arc090_b
# tag: グラフ 連結成分 重み付きUnion-Find 典型問題

# 重み付きUnion-Findを用いると簡単に解ける典型問題。

class Weighted_Union_Find:
    def __init__(self, N):
        self.parent = [-1] * N
        self.rank = [0] * N
        self.weight = [0] * N
        self.group_count = N
        self.N = N

    #最上位の親(グループリーダー)を取得
    def find(self, x):
        # parent が負数なら、自分がリーダー
        if self.parent[x] < 0:
            return x

        # 自分をリーダーの直下に置き直し、重み付けを更新するのを
        # 再帰で根本まで行う
        leader = self.find(self.parent[x])
        self.weight[x] += self.weight[self.parent[x]]
        self.parent[x] = leader

        return leader

    # xとyのグループを統合しつつ、(統合先リーダー, 統合元リーダー)を返す
    # 統合不要なら(-1, -1)を返し、矛盾する値が来たらエラーを返す
    def unite(self, x, y, w):
        lx, ly = self.find(x), self.find(y)

        # そもそも同じグループにいる場合、何もしない
        if lx == ly:
            # が、値が矛盾する場合はエラーを返す
            if self.get_diff(x, y) != w:
                raise ValueError ('value contradiction detected')
            else:
                return (-1, -1)
    
        lx_to_ly = self.weight[x] - self.weight[y] + w
        self.group_count -= 1

        # 同じ高さのときは、とりあえず x の下に y をつけ、高さを更新
        if self.rank[lx] == self.rank[ly]:
            self.parent[ly] = lx
            self.weight[ly] = lx_to_ly
            self.rank[x] += 1
            return (lx, ly)
        
        # 高さが違う場合は、高い方に低い方をつける
        if self.rank[lx] < self.rank[ly]:
            lx, ly = ly, lx
            lx_to_ly = - lx_to_ly
        
        self.parent[ly] = lx
        self.weight[ly] = lx_to_ly
        return (lx, ly)

    # 同じリーダーの下なら（＝比較可能なら）距離を返す
    # 違ったら None を投げておく
    def get_diff(self, x, y):
        if self.find(x) == self.find(y):
            return self.weight[y] - self.weight[x]
        else:
            return None

def main():
    N, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(M)]

    wuft = Weighted_Union_Find(N+1)

    for x, y, w in info:
        try:
            wuft.unite(x, y, w)
        except ValueError:
            print('No')
            return
    else:
        print('Yes')

main()
