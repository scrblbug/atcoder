# AtCoder Beginner Contest 192 E - Train
# https://atcoder.jp/contests/abc192/tasks/abc192_e
# tag: グラフ ダイクストラ法 最短距離 AtCoder国

# ダイクストラ法で解ける問題だが、次の地点への
# コストを求める際、列車の待ち時間を考慮してやる
# 必要があるので注意。

from heapq import heappush, heappop
def main():
    N, M, X, Y = map(int, input().split())
    trains = [list(map(int, input().split())) for _ in range(M)]

    # 下準備
    paths = [[] for _ in range(N)]
    for a, b, t, k in trains:
        a -= 1
        b -= 1
        paths[a].append((b, t, k))
        paths[b].append((a, t, k))

    X -= 1
    Y -= 1

    # ダイクストラ法で最短コストを求めていく。
    # ここではグラフのコストを早めに更新していく、
    # 若干変形したダイクストラ法を用いている。
    # 教科書的なダイクストラ法を用いた場合については後述。
    dist = [-1] * N
    dist[X] = 0
    queue = [(0, X)]

    while queue:
        dist_now, now = heappop(queue)
        if dist_now > dist[now]:
            continue
        for nxt, t, k in paths[now]:
            # 次の列車までの待ち時間を求める。
            if dist_now % k == 0:
                wait = 0
            else:
                wait = k - dist_now % k

            # 次の地点への到着時刻は、現在時刻＋待ち時間＋移動時間
            dist_nxt = dist_now + wait + t

            if dist[nxt] == -1 or dist_nxt < dist[nxt]:
                # あらかじめ緩和しておくと、heapq の使用回数が
                # 少なくなり、若干速くなる。
                dist[nxt] = dist_nxt

                heappush(queue, (dist_nxt, nxt))

    print(dist[Y])

main()


