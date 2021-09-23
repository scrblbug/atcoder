# AtCoder Beginner Contest 208 D - Shortest Path Queries 2
# https://atcoder.jp/contests/abc208/tasks/abc208_d
# tag: ワーシャル・フロイド法 考察 高橋王国

# この問題の形は、ワーシャル・フロイド法における
# 計算過程を示したものとなっている。

# よって、通常通りワーシャル・フロイド法を回しつつ、
# 随時回答へと距離を足し合わせていく。

def main():
    N, M = map(int, input().split())
    dist_dat = [list(map(int, input().split())) for _ in range(M)]

    dist = [[10**10] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0

    for a, b, c in dist_dat:
        a -= 1
        b -= 1
        dist[a][b] = c

    result = 0
    # ワーシャル・フロイド法。
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

                # 到達可能なら、答えに足し合わせる。
                if dist[i][j] != 10**10:
                    result += dist[i][j]

    print(result)

main()
