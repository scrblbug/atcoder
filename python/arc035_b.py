# AtCoder Regular Contest 035 B - アットコーダー王国のコンテスト事情
# https://atcoder.jp/contests/arc035/tasks/arc035_b
# tag: 考察 事前ソート MOD

# 仮に全 3 問、かかる時間がそれぞれ a, b, c とすると、
# 全体のペナルティは a + (a + b) + (a + b + c)
# = 3 * a + 2 * b + c
# となることから分かるように、早めに解いた問題の方が
# 何度も時間として加算されることになる。

# よって、掛かる時間が短い問題から順番に解くのがいい。

# 通り数については、掛かる時間が同じ問題についてのみ
# 入れ替え可能で、かつどのような順に解いてもいい。
# つまり、ある時間で解ける問題が n 問あるとしたとき、
# n! 通りの解き方があることになる。

from collections import Counter
def main():
    N = int(input())
    spends = [int(input()) for _ in range(N)]
    MOD = 10**9 + 7

    # あらかじめ階乗を求めておく
    fact = [1]
    for i in range(1, N+1):
        fact.append((fact[-1] * i) % MOD)

    # 時間が掛からない順に並べておく
    spends.sort()

    # 最初から順に N 回, N-1 回, N-2 回足されることになる
    result1 = 0
    for i, t in enumerate(spends):
        result1 += t * (N - i)

    # 掛かる時間ごとにカウントし、その階乗を掛けていく
    cnt = Counter(spends)
    result2 = 1
    for v in cnt.values():
        result2 = (result2 * fact[v]) % MOD

    print(result1)
    print(result2)

main()
