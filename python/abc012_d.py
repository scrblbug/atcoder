# AtCoder Beginner Contest 012 D - バスと避けられない運命
# https://atcoder.jp/contests/abc012/tasks/abc012_4
# tag: ワーシャル・フロイド法 典型問題 高橋君

# 結局のところ各バス停間全通りの移動コストを確認する
# 必要があるので、ワーシャル・フロイド法を用いる。

# あとは、バス停ごとに最大コストを比較すればいい。

def main():
    N, M = map(int, input().split())
    bus_dat = [list(map(int, input().split())) for _ in range(M)]

    # 0-indexed に修正しつつ、移動時間の隣接行列を作成する。
    dist = [[10**10] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for a, b, t in bus_dat:
        a -= 1
        b -= 1
        dist[a][b] = t
        dist[b][a] = t

    # ワーシャル・フロイド法
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # 改めて、各バス停ごとの最大コストの最小値を求める。
    result = min(max(dist[i]) for i in range(N))
    print(result)

main()
