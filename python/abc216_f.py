# AtCoder Beginner Contest 216 F - Max Sum Counting
# https://atcoder.jp/contests/abc216/tasks/abc216_f
# tag: 事前ソート DP

# DP がやや難しいので、可能な限りわかりやすく、
# 分解して書いてみた。

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353

    ab = [(a, b) for a, b in zip(A, B)]
    ab.sort()

    dpt = [[0] * 5001 for _ in range(N+1)]
    dpt[0][0] = 1


    # dpt[i][j]: 数列 B の i 番目までの数で、
    # 合計がちょうど数 j になるような部分集合の通り数。
    for i in range(1, N+1):
        a, b = ab[i-1]
        for j in range(5001):
            dpt[i][j] = dpt[i-1][j]

            if b <= j:
                dpt[i][j] += dpt[i-1][j-b]
                dpt[i][j] %= MOD

    # 累積和を取る。
    # dpt[i][j]: 数列 B の i 番目までの数で、
    # 合計が j 以下になるような部分集合の通り数。
    for i in range(N+1):
        tmp = 0
        for j in range(5001):
            tmp += dpt[i][j]
            dpt[i][j] = tmp

    result = 0

    # 数列 A の中の数 a を含み、条件を満たすものは
    # 一つ手前までの数において、B の部分集合の合計が
    # a - b 以下になっている通り数。
    for i, (a, b) in enumerate(ab, start=1):
        if a >= b:
            result = (result + dpt[i-1][a-b]) % MOD

    print(result)


main()

