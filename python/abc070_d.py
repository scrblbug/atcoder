# AtCoder Beginner Contest 070 D - Transit Tree Path
# https://atcoder.jp/contests/abc070/tasks/abc070_d
# tag: グラフ 木 最短距離 典型問題

# x から、K を経由しつつ y に行く最短距離を求めるためには、
# x → K の最短距離と、K → y の最短距離が必要。

# ところで、今回の問題のグラフは方向が関係ない無向グラフに
# なっているので、x → K の最短距離と、K → x の最短距離は
# 等しい。

# つまり、クエリがなんであれ、K からすべての頂点への
# 最短経路が求まっていれば、O(1) で回答を得ることが可能。

# K からの最短距離については、グラフが木であることから、
# 単純に順番に確定していけば、それが最短距離になる。

def main():
    N = int(input())
    path_dat = [list(map(int, input().split())) for _ in range(N-1)]
    Q, K = map(int, input().split())
    K -= 1
    queries = [list(map(int, input().split())) for _ in range(Q)]

    paths = [[] for _ in range(N)]
    for a, b, c in path_dat:
        a -= 1
        b -= 1
        paths[a].append((b, c))
        paths[b].append((a, c))

    # 頂点 K からの距離を保存していく。
    dist = [-1] * N
    dist[K] = 0

    # 探索しつつ距離を決定していく。
    queue = [K]
    while queue:
        now = queue.pop()
        for nxt, dd in paths[now]:
            # 距離を確定済み＝探索済みならスキップ。
            if dist[nxt] != -1:
                continue
            dist[nxt] = dist[now] + dd
            queue.append(nxt)

    # クエリ処理
    for x, y in queries:
        x -= 1
        y -= 1
        print(dist[x] + dist[y])

main()
