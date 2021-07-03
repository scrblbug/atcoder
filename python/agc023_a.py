# AtCoder Grand Contest 023 A - Zero-Sum Ranges
# https://atcoder.jp/contests/agc023/tasks/agc023_a
# 数列 連続部分列 順列・組み合わせ 数え上げ 累積和

# 連続部分列の総和なので、とりあえず累積和を用いることを考える。
# 入力例 1 を具体例とすると、

# A: [1, 3, -4, 2, 2, -2]

# この累積和を取ると（初項を 0 とする）
# csum: [0, 1, 4, 0, 2, 4, 2]

# さて、連続部分列を A[i:j] とした場合、
# その総和は、csum[j] - csum[i] となる。

# つまり、累積和を数列として考えた場合、
# 同じ数字が現れる場所 (i, j) があれば、
# そこに相当する連続部分列の総和を 0 に出来る。

# よって、問題の回答は累積和の数列における、
# 同じ数字の組み合わせ数に帰着できる。

from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 累積和を取る
    csum = [0]
    for a in A:
        csum.append(csum[-1] + a)

    # 累積和の中で現れる数をカウント
    cnt = Counter(csum)

    # ある数字が n 回現れていれば、
    # そのうち2個の組み合わせ数は n(n-1)/2 となる
    result = 0
    for n in cnt.values():
        result += n * (n-1) // 2

    print(result)

main()
