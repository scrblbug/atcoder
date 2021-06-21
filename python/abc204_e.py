# AtCoder Beginner Contest 204 E - Rush Hour 2
# https://atcoder.jp/contests/abc204/tasks/abc204_e
# tag: グラフ 最小コスト 考察 ダイクストラ法

from heapq import heappop, heappush
def main():
    N, M = map(int, input().split())
    path_dat = [list(map(int, input().split())) for _ in range(M)]

    paths = [[] for _ in range(N)]
    for a, b, c, d in path_dat:
        a -= 1
        b -= 1
        paths[a].append((b, c, d))
        paths[b].append((a, c, d))
    
    # ここからダイクストラ法
    # 始点からのコストを管理
    dist = [10**18] * N
    dist[0] = 0

    # 優先度付きキュー (始点からのコスト, ノード番号)
    hq = [(0, 0)]

    while hq:
        dist_now, now = heappop(hq)
        if dist_now > dist[now]:
            continue

        # 次のノード nxt に到着する最小の時間を求める
        for nxt, c, d in paths[now]:
            # とりあえず即出発した場合を初期値にする
            dist_nxt = dist_now + c + (d // (dist_now+1))

            # sqrt(d) 近傍に最小値があるっぽいので、付近を探索
            mid = int(d**0.5)
            # departure: 出発予定時間とする
            for departure in range(mid - 3, mid + 3):
                # 出発予定時間が今の時刻より早ければ、飛ばす
                if departure <= dist_now:
                    continue
                tmp = departure + c + (d // (departure+1))
                if tmp < dist_nxt:
                    dist_nxt = tmp
            
            # 最小コストを更新したら、グラフを緩和してキューに追加
            if dist_nxt < dist[nxt]:
                dist[nxt] = dist_nxt
                heappush(hq, (dist_nxt, nxt))
    
    if dist[N-1] == 10**18:
        print(-1)
    else:
        print(dist[N-1])

main()