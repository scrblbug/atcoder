# AtCoder Beginner Contest 132 D - Blue and Red Balls
# https://atcoder.jp/contests/abc132/tasks/abc132_d
# tag: 数え上げ 二項定理 パスカルの三角形 MOD 順列・組み合わせ

# 青が i 個の塊になっている必要がある。
# 仮に i = 2 の場合の通り数を見つつ、一般化を試みる。

# 最終的には、
# (0個以上の赤) (1個以上の青) (1個以上の赤) (1個以上の青) (0個以上の赤)
# となっている必要がある。

# あらかじめ 1 個以上必要なところに 1 個置いておくとすると、
# i 個の青と i-1 個の赤が配置済みになる。
# その上で考える必要があるのは、
# n: 残った K-i 個の青を、i 個の場所へと重複ありで置く通り数
# m: 残った N-K-(i-1) 個の赤を、i+1 個の場所へと重複ありで置く通り数
# この n * m が、最終的な通り数となる。

# これらはそれぞれ
# n = (K-i + (i-1))! / ((K-i)! (i-1)!)
#   = (K-1)! / ((K-i)! (i-1)!)
#   = K-1 C i-1

# m = (N-K-(i-1) + i+1-1)! / ((N-K-(i-1) + i+1-1)! (i+1-1)!)
#   = (N-K+1) / ((N-K+1)! i!)
#   = N-K+1 C i

# これを素早く求められるように、あらかじめパスカルの三角形を
# 用いて準備しておく。

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7

    # パスカルの三角形を用いて、
    # comb[i][j] = i C j となるようなテーブルを
    # 作成しておく。
    comb = [[0] * (N+1) for _ in range(N+1)]
    comb[0][0] = 1
    for i in range(1, N+1):
        for j in range(N+1):
            if j == 0:
                comb[i][j] = 1
            else:
                comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD

    # 考察より、答えを求める。
    for i in range(1, K+1):
        result = (comb[K-1][i-1] * comb[N-K+1][i]) % MOD
        print(result)

main()
