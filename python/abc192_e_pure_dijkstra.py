# 教科書的なダイクストラ法の書き方だと、以下のような感じになる。

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
    dist = [-1] * N
    queue = [(0, X)]

    while queue:
        dist_now, now = heappop(queue)
        if dist[now] != -1:
            continue
        dist[now] = dist_now
        for nxt, t, k in paths[now]:
            # 次の列車までの待ち時間を求める。
            if dist_now % k == 0:
                wait = 0
            else:
                wait = k - dist_now % k

            # 次の地点への到着時刻は、現在時刻＋待ち時間＋移動時間
            dist_nxt = dist_now + wait + t

            heappush(queue, (dist_nxt, nxt))

    print(dist[Y])

main()
