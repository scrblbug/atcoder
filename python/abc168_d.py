# AtCoder Beginner Contest D - ..(Double Dots)
# https://atcoder.jp/contests/abc168/tasks/abc168_d
# tag: グラフ BFS 典型問題

# 部屋を頂点、通路を辺とするグラフを作成する。
# 問題の設定とは逆に、部屋1 からスタートすると考え、
# BFSでそれぞれの部屋への最短距離を求めていく。
# 全ての部屋が連結していれば、求めた各最短距離から
# 逆算して道標を置いていく。

from collections import deque
def main():
    N, M = map(int, input().split())
    path_dat = [list(map(int, input().split())) for _ in range(M)]
    
    # 各部屋から伸びる辺を管理する
    # 0-indexed に変換しておく
    paths = [[] for _ in range(N)]
    for a, b in path_dat:
        paths[a-1].append(b-1)
        paths[b-1].append(a-1)

    # スタートを 0 として、部屋 0 からの距離を格納するリスト
    # -1 は未到達
    dist = [-1] * N
    dist[0] = 0

    # BFS で各部屋への距離を求める
    queue = deque([0])
    while queue:
        now = queue.popleft()
        for nxt in paths[now]:
            if dist[nxt] != -1:
                continue
            dist[nxt] = dist[now] + 1
            queue.append(nxt)

    # 各部屋の距離を確認し、つながっている部屋のうち
    # 自身の距離より小さい距離のところへの道標を置く
    sign = [-1] * N
    for now in range(1, N):
        # 距離が測定できなかった部屋＝部屋 0 とつながっていない部屋が
        # あれば、No を出力して終了する
        if dist[now] == -1:
            print('No')
            return
        for nxt in paths[now]:
            # 候補が見つかれば、そこへの道標を置く
            if dist[nxt] == dist[now] - 1:
                sign[now] = nxt
                break

    # 回答を出力する。0-indexed を 1-indexed に訂正しておくこと
    print('Yes')
    for room in range(1, N):
        print(sign[room] + 1)

main()
