# AtCoder Beginner Contest 223 D - Restricted Permutation
# https://atcoder.jp/contests/abc223/tasks/abc223_d
# tag: 数列 辞書順 優先度付きキュー トポロジカルソート

# Ai が Bi より先に現れるとのことなので、
# 各 Ai → Bi の辺を持つグラフで考えてみる。

# すると、取ることができる頂点は、入辺の無い頂点になる。
#  そのうち、辞書順で一番小さな頂点と、出ている辺を削除する。
# ……といった操作を繰り返すことで、答えを求めることが可能。

# 実装としては、常に辞書順最小の頂点を取る必要があるので、
# ここに優先度付きキューを使用する。

# つまり、優先度付きキューの中に、取ることができる頂点を
# どんどん追加していくイメージ。

# 取ることができる頂点については、各頂点ごとの入辺数を
# 管理する。頂点を取り除く際は、取り除いた頂点の出辺先にある
# 頂点の入変数を 1 引いてやればよい。

from heapq import heapify, heappush, heappop
def main():
    N, M = map(int, input().split())
    path_dat = [list(map(int, input().split())) for _ in range(M)]

    # 0-indexed
    paths = [[] for _ in range(N)]

    # 入辺数をを管理する。
    path_in = [0] * N

    # グラフを構築しながら、入辺数を数えておく。
    for a, b in path_dat:
        a -= 1
        b -= 1
        paths[a].append(b)
        path_in[b] += 1

    # 取り除ける頂点集合。優先度付きキューにしておく。
    available = [n for n in range(N) if path_in[n] == 0]
    heapify(available)

    result = []

    while available:
        # 辞書順最小の、取り除ける頂点を答えに追加。
        now = heappop(available)
        result.append(now + 1)

        # 次の頂点の入辺数から 1 を引き、0 になったら available に追加。
        for nxt in paths[now]:
            path_in[nxt] -= 1
            if path_in[nxt] == 0:
                heappush(available, nxt)

    # 全てが取り除けなかった場合は、P が存在しない。
    if len(result) != N:
        print(-1)
    else:
        print(*result)

main()
