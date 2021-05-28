# AtCoder Grand Contest 031 A - Colorful Subsequence
# https://atcoder.jp/contests/agc031/tasks/agc031_a
# tag: 文字列 部分文字列 順列・組み合わせ 数え上げ 考察 MOD

# 文字の種類別に考えると、ある文字種 ch が n 回文字列に
# 現れている場合、その文字をとりだす通り数は、n 箇所の
# どこかから取り出す or 取り出さないという n+1 通り。
# これらを文字種別に独立して行うことができる。

# ただし、すべての文字を取り出さない場合、すなわち
# 空文字列になってしまう 1 通りは除外する必要がある。

from collections import Counter
def main():
    N = int(input())
    S = input()
    MOD = 10**9 + 7

    # 文字種別に数えておく
    cnt = Counter(S)

    result = 1

    # 文字種別に 個数+1 を掛けていく
    for cn in cnt.values():
        result = (result * (cn + 1)) % MOD

    # 空文字列の場合を引く
    result -= 1

    print(result)

main()
