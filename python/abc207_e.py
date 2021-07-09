# AtCoder Beginner Contest 207 E - Mod i
# https://atcoder.jp/contests/abc207/tasks/abc207_e
# tag: 整数 倍数 剰余 DP 累積和

# どのようなものが分かっていれば答えが求まるかから、
# DP を決定する。

# 左から順に決定していくとして、

# dpt[i][j]: A[j] までを条件に合うように i個に分割する通り数

# このとき i-1 → i への遷移を考えると、
# dpt[i][j] = sum(dpt[i-1][l])
# ここで l は、sum(A[l+1:j]) % i == 0 となるような
# j 未満の全ての l

# sum(A[l+1:j]) % i == 0 となる条件とは、
# csum[j] % i == csum[l] % i となること

# 以上から、この合計は剰余別の一種の累積和として管理でき、
# 左から順に求めていくことができる。

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7

    csum = [0] * N
    tmp = 0
    for i, a in enumerate(A):
        tmp += a
        csum[i] = tmp

    # DP の初期化
    dpt = [[0] * N for _ in range(N+1)]

    # 分割数 1 なら、かならず 1 通り
    for j in range(N):
        dpt[1][j] = 1

    for i in range(2, N+1):
        # dpt_mod[m]: csum[l] % i == m となるような、
        # j 未満の l における dpt[i-1][l] の合計とする
        dpt_mod = [0] * i

        for j in range(N):
            m = csum[j] % i
            dpt[i][j] = (dpt[i][j] + dpt_mod[m]) % MOD

            # 最後に dpt_mod を更新することで、
            # dpt_mod は次回検討する j+1 未満の dpt[i-1][l] の合計となる
            dpt_mod[m] = (dpt_mod[m] + dpt[i-1][j]) % MOD
    
    result = 0
    for i in range(N+1):
        result += dpt[i][-1]
    
    print(result % MOD)

main()



