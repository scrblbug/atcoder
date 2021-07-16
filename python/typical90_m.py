# 競プロ典型90問 013 - Passing
# https://atcoder.jp/contests/typical90/tasks/typical90_m
# tag: グラフ 最短距離 ダイクストラ法 AGC王国

from heapq import heappush, heappop
def main():
    N, M = map(int, input().split())
    path_dat = [list(map(int, input().split())) for _ in range(M)]

    paths = [[] for _ in range(N)]
    for a, b, d in path_dat:
        a -= 1
        b -= 1
        paths[a].append((b, d))
        paths[b].append((a, d))

    def dijkstra(start):
        queue = [(0, start)]
        dist = [-1] * N

        while queue:
            dist_now, now = heappop(queue)
            if dist[now] != -1:
                continue
            dist[now] = dist_now

            for nxt, dd in paths[now]:
                if dist[nxt] != -1:
                    continue
                dist_nxt = dist_now + dd
                heappush(queue, (dist_nxt, nxt))

        return dist

    dist_from_start = dijkstra(0)
    dist_from_goal = dijkstra(N-1)

    for i in range(N):
        print(dist_from_start[i] + dist_from_goal[i])
    
main()

