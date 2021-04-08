# AtCoder Beginner Contest 022 C - Blue Bird
# https://atcoder.jp/contests/abc022/tasks/abc022_c
# tag: グラフ 距離 ワーシャル・フロイド法 高橋君

# そのまま最短距離を求めていくのは難しいので、経路を分割して考える。
# すなわち、高橋君の家の隣の頂点 u, v (u != v) を適当に決め、
# 高橋君の家 ～ u ～ v ～ 高橋君の家
# という経路を、 (u, v) の組み合わせで全探索する。

# その際、あらかじめ高橋君の家を含まないグラフを用い、
# ワーシャル・フロイド法で u ～ v の経路について
# あらかじめ最短距離を全て求めておく。

def main():
    N, M = map(int, input().split())
    path_dat = [list(map(int, input().split())) for _ in range(M)]

    # 距離の隣接行列
    # これをワーシャル・フロイド法で緩和していく
    dist = [[10**10] * N for _ in range(N)]

    # 高橋君の家のすぐ隣の頂点と、その距離を保存
    dist_n = dict()

    # 下準備
    for i in range(N):
        dist[i][i] = 0

    # 高橋君の家 ～ その隣の頂点への道と、それ以外とを
    # 別に管理する。
    for u, v, l in path_dat:
        u -= 1
        v -= 1
        if u != 0 and v != 0:
            dist[u][v] = l
            dist[v][u] = l
        else:
            dist_n[max(u, v)] = l

    # ワーシャル・フロイド法
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    result = 10**10

    # 高橋君の家 ～ 頂点 u ～ 頂点 v ～ 高橋君の家 (u != v) の
    # 最小値を全探索で求める
    neighbors = list(dist_n.keys())
    for i in range(len(neighbors) - 1):
        for j in range(i+1, len(neighbors)):
            d = dist_n[neighbors[i]] + dist[neighbors[i]][neighbors[j]] + dist_n[neighbors[j]]
            if d < result:
                result = d

    if result >= 10**10:
        print(-1)
    else:
        print(result)

main()
