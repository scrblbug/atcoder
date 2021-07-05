# AtCoder Beginner Contest 170 D - Not Divisible
# https://atcoder.jp/contests/abc170/tasks/abc170_d
# tag: 整数 倍数 計算量 コーナーケース

# この問題は、計算量を考えた時に、 
# O(N + N//2 + ... + 1) = O(N logN)
# となることを知っていないと厳しい。

# 入力例にもある通り、同じ数字が存在する場合があるので、
# そこも処理してやる必要がある。

# ここではあまり速さにはこだわらず、素直な解き方で書いてみる。
# が、逆に言うとこの書き方でも十分間に合う。
from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))

    limit = max(A) + 1

    # not_divisible[n] = True の時、n は問題の条件に合うとする
    not_divisible = [False] * limit

    cnt = Counter(A)

    # 初期化。ダブっていない数字を True にセット
    for a in cnt.keys():
        if cnt[a] == 1:
            not_divisible[a] = True

    # 全ての数字について、その倍数を False にしていく
    for a in cnt.keys():
        for i in range(a*2, limit, a):
            not_divisible[i] = False

    # あとは残っているものを数えるだけ
    result = sum(not_divisible)
    print(result)

main()
