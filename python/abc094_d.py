# AtCoder Beginner Contest 094 D - Binomial Coefficients
# https://atcoder.jp/contests/abc094/tasks/arc095_b
# tag: 順列・組み合わせ 基礎問題 二項係数

# 組み合わせ数の、ごく基本的な性質を訊かれている問題。

# n C r つまり n 個から 順番に関係なく r 個を選ぶ場合の数は、
# 1) r が同じなら n が大きいほど大きくなり、
# 2) n が同じなら r が n / 2 に近づくほど大きくなる。

# 以下、厳密な証明ではないが……

# 1) に関しては選ぶ元の個数が増えるので明らか。

# 2) に関しては、基本的には選ぶ個数 r が増えるほど、元の選び方に加えて
# 追加のものの選び方も加わるため、n C r は大きくなる。
# ただし、r 個選ぶのは、残りの n-r 個を選ぶという行為と等しい。
# つまり、n C r は n C (n-r) に等しくなる。
# 以上の2点をふまえ、r が変化するときの n C r の極大は r = n / 2 の時。

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 一番大きな数字を n に
    n = max(A)

    # n の半分に一番近い数字を r に
    mid = n / 2
    r = 0
    for a in A:
        if abs(a - mid) < abs(r - mid):
            r = a

    print(n, r)

main()
