# AtCoder Beginner Contest 219 D - Strange Lunchbox
# https://atcoder.jp/contests/abc219/tasks/abc219_d
# tag: DP 高橋君

# 典型的な DP 問題。
# DP[i][j][k]:
# 今 i-1 個目の弁当を購入するかどうか検討しているとき、
# これまでにたこ焼き j 個とたい焼き k 個を入手するのに
# 必要な弁当の数の最小値。

# たこ焼き・たい焼きが(a, b)入っている弁当を
# 購入する場合は、
# DP[i+1][j+a][k+b] = min(DP[i+1][j+a][k+b], DP[i][j][k] + 1)
# ただし、j + a と k + b は上限 X, Y でキャップしてやる
# 必要がある。

# 購入しない場合は、
# DP[i+1][j][k] = min(DP[i+1][j][k], DP[i][j][k])

# 二次元配列を更新しながら、弁当を買う場合と買わない場合を
# 検討していくようなイメージ。

def main():
    N = int(input())
    X, Y = map(int, input().split())
    boxes = [list(map(int, input().split())) for _ in range(N)]

    dpt = [[[-1] * (Y+1) for _ in range(X+1)] for _ in range(N+1)]

    dpt[0][0][0] = 0

    for i, (a, b) in enumerate(boxes):
        for j in range(X+1):
            for k in range(Y+1):
                if dpt[i][j][k] == -1:
                    continue

                # 購入するとき
                new_tak = min(X, j + a)
                new_tai = min(Y, k + b)
                if dpt[i+1][new_tak][new_tai] > dpt[i][j][k] + 1 or dpt[i+1][new_tak][new_tai] == -1:
                    dpt[i+1][new_tak][new_tai] = dpt[i][j][k] + 1

                # 購入しない時
                if dpt[i+1][j][k] > dpt[i][j][k] or dpt[i+1][j][k] == -1:
                    dpt[i+1][j][k] = dpt[i][j][k]

    print(dpt[N][X][Y])

main()


