# AtCoder Beginner Contest 160 D - Line++
# https://atcoder.jp/contests/abc160/tasks/abc160_d
# tag: グラフ BFS 距離 数え上げ

# 最初に思いついたのは、それぞれの開始地点から、BFSで全探索。
# 制約 (3 <= N <= 2000) で、O(N^2) なのでちゃんと間に合う。
# Pypyなら230msくらいで余裕。Python提出でも1300msくらい。
# あまり何も考えずに書けるので、まあこれでもいいのでは？……という感じ。

from collections import deque
def main():
    # 内部的には 0-indexed にしておく
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1

    # グラフ構築
    paths = [[] for _ in range(N)]
    for i in range(N-1):
        paths[i].append(i+1)
        paths[i+1].append(i)
    paths[X].append(Y)
    paths[Y].append(X)

    # 最短距離ごとの組み合わせ数を探索の際に数えていく
    # result[x]: 最短距離 x の組み合わせ数
    result = [0] * N

    # 開始地点 (1 ～ N) を全部試す
    for start in range(N):
        dist = [-1] * N
        dist[start] = 0
        queue = deque([start])

        # いつものBFS
        while queue:
            now = queue.popleft()
            for nxt in paths[now]:
                if dist[nxt] != -1:
                    continue
                dist[nxt] = dist[now] + 1
                queue.append(nxt)

                # 距離が確定した際、result で数えておく
                result[dist[nxt]] += 1

    # 往復で数えているので、2 で割って出力
    for r in result[1:]:
        print(r//2)

# main()

# 公式解説のやり方は、開始地点と終了地点を定めての全探索。
# 距離については、経路(X-Y) を通る場合と通らない場合で
# 分けてやると、O(1) で計算できる。
# さっきのやり方は往復で見てしまっている分無駄があるので、
# こちらのほうが速い。
# 実際に（最大効率で書けば）大体半分の実行時間になるのが、
# ちょっと面白い（当たり前ではあるが）。

def main2():
    N, X, Y = map(int, input().split())

    # ここでは、関数を分けて少し分かりやすく書いている
    def get_dist(a, b):
        # a -> b 直行
        d1 = abs(a - b)

        # a -> X -> Y -> b
        d2 = abs(a - X) + 1 + abs(b - Y)

        # a -> Y -> X -> b
        d3 = abs(a - Y) + 1 + abs(b - X)

        # 経路は上記のどれかになるので、最小のものを返す
        return min(d1, d2, d3)

    result = [0] * N

    for start in range(1, N):
        for goal in range(start+1, N+1):
            result[get_dist(start, goal)] += 1

    for r in result[1:]:
        print(r)

# main2()
