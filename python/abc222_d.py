# AtCoder Beginner Contest 222 D - Between Two Arrays
# https://atcoder.jp/contests/abc222/tasks/abc222_d
# tag: 数列 単調増加 MOD 数え上げ DP 累積和 典型問題

# 典型的なDPの問題。
# dpt[i][j]: i 番目の数字までを確定したとき、C の最後の数字が
# j であるような数列の通り数とする。

# このとき、dpt[i+1][j] は dpt[i][0] ～ dpt[i][j]の合計となる。
# （ただし、A[i-1] <= j <= B[i-1])

# C のある場所の数字を v と決定するとき、
# ひとつ前の数字は v 以下である必要がある。
# よって、ひとつ前の数字が 1 ～ v のそれぞれの
# 通り数を合計したものが、現在の通り数となる、ということ。

# DP 時は、累積和を取りながら回してやるとよい。

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353

    dpt = [[0] * 3001 for _ in range(N+1)]

    # 初期値。
    dpt[0][0] = 1

    for i in range(1, N+1):
        # 累積和を取る
        tot = 0

        for j in range(3001):
            tot = (tot + dpt[i-1][j]) % MOD

            # 範囲を越えたら終了し、次の数字へ。
            if j > B[i-1]:
                break

            # 範囲内なら、dpt を更新する。
            if j >= A[i-1]:
                dpt[i][j] = tot

    print(sum(dpt[-1]) % MOD)

main()
