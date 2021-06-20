# AtCoder Beginner Contest 206 D - KAIBUNsyo
# https://atcoder.jp/contests/abc206/tasks/abc206_d
# tag: 数列 回文 グラフ 連結成分 BFS DFS Union_Find

# a b c d e f g という数列と仮定して考えてみる。
# 回文にするためには、(a b c) と (g f e) を一致させる
# 必要がある。

# つまり、a-g b-f c-e に関してはそれぞれどちらかを
# 変更し、統一する必要があるということ。

# ところで、同じことを入力例1 について考えてみると、
# (1 5 3 2) と (1 3 2 5) を一致させることになり、
# 1-1 5-3 3-2 2-5 という対応が起こることになる。
# この場合、5-3-2 は最終的に全て同じ数字に変換されなければ
# ならないことになる。

# ここで、N 種類の数字を全て同じに変更するためには、
# 元の N 種類のうちどれか一種類にあわせるとして、
# 最短でも N-1 回の変換を行う必要がある。

# 以上を踏まえると……
# 全ての対応を洗い出し、各数字を頂点としてグラフを構築。
# 連結成分ごとに、(要素数 - 1) 回の変換を行うことで
# 最終的な目標を達成できる。

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # リストの前半とreversed(後半) を用意する。
    former = A[:N//2]
    latter = list(reversed(A[-N//2:]))

    # 先程のリストを元に、対応する数字一覧を作成する。
    path_dat = set()
    for f, l in zip(former, latter):
        path_dat.add((min(f, l), max(f, l)))

    # 一覧を元にグラフを構築。制約上限で作っておく。
    paths = [[] for _ in range(2 * 10**5 + 1)]
    for a, b in path_dat:
        paths[a].append(b)
        paths[b].append(a)

    result = 0

    visited = [False] * (2 * 10**5 + 1)

    # 連結成分ごとに探索を行う（BFSでもDFSでも良い）
    for start in range(2 * 10**5 + 1):
        if visited[start]:
            continue
        visited[start] = True
        queue = [start]

        # 連結成分の要素数
        cnt = 1

        # 探索開始（ここではDFS）
        while queue:
            now = queue.pop()
            for nxt in paths[now]:
                if visited[nxt]:
                    continue
                visited[nxt] = True
                cnt += 1
                queue.append(nxt)

        # 考察に従い、(要素数 - 1) を答えに加算
        result += cnt - 1

    print(result)

main()

# 上記の考察による回答は、連結成分を管理できればいいので、
# Union_Find によっても実装することができる。
# 特に連結成分数を管理できるように作っておくと楽。

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

### ここから main
def main2():
    N = int(input())
    A = list(map(int, input().split()))

    # リストの前半とreversed(後半) を用意する。
    former = A[:N//2]
    latter = list(reversed(A[-N//2:]))

    # 先程のリストを元に、対応する数字一覧を作成する。
    path_dat = set()
    for f, l in zip(former, latter):
        path_dat.add((min(f, l), max(f, l)))

    # 制約一杯で Union_Find木 を作成する。
    uft = Union_Find(2 * 10**5 + 1)

    # 対応する数字を連結していく。
    for a, b in path_dat:
        uft.unite(a, b)

    # 各連結成分の (要素数 - 1) の合計 ＝
    # 全体の要素数 - 連結成分の個数
    # となるので……
    print(2 * 10**5 + 1 - uft.group_count)

# main2()
