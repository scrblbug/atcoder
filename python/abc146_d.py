# AtCoder Beginner Contest 146 D - Coloring Edges on Tree
# https://atcoder.jp/contests/abc146/tasks/abc146_d
# tag: グラフ 木 色塗り 貪欲法

# 各頂点から伸びる辺の色が全て異なるようにする。
# 木なので、適当に根を定めて条件に合うように順に塗っていく
# 貪欲法でいい。

def main():
    N = int(input())
    path_dat = [list(map(int, input().split())) for _ in range(N-1)]

    paths = [[] for _ in range(N)]
    for u, v in path_dat:
        u -= 1
        v -= 1
        paths[u].append(v)
        paths[v].append(u)

    # 辺ごとに塗った色を管理していく。
    # colors[(u, v)] = 塗った色 とする。(u < v)
    colors = dict()

    # 探索しつつ、頂点ごとに全ての辺の色を決定していく。
    # 親から降りてくる際の辺だけはあらかじめ決定済みになる。
    queue = [(-1, 0)]
    while queue:
        prev, now = queue.pop()

        # 根で無ければ、親から降りてきた際の辺の色を
        # used として確認しておく。
        if prev != -1:
            u, v = min(prev, now), max(prev, now)
            used = colors[(u, v)]
        else:
            used = -1

        # 辺ごとに色をつけていく。色はとりあえず 1 から使う。
        col = 1
        for nxt in paths[now]:
            if nxt == prev:
                continue
            # 親からの辺と色が重複したら、次の色を使う。
            if col == used:
                col += 1
            
            # 色づけ。colors へ保存しておく。
            u, v = min(now, nxt), max(now, nxt)
            colors[(u, v)] = col
            col += 1
            queue.append((now, nxt))

    # 使用した色数を出力。
    print(max(colors.values()))

    # 辺ごとの色を出力。
    for u, v in path_dat:
        u -= 1
        v -= 1
        if u > v:
            u, v = v, u
        print(colors[(u, v)])

main()
