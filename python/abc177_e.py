# AtCoder Beginner Contest 177 E - Coprime
# https://atcoder.jp/contests/abc177/tasks/abc177_e
# tag: 整数 最大公約数 計算量

# 全ての数の最大公約数が 1 かどうかを確認するのは簡単。
# 問題は、全ての組み合わせの最大公約数が 1 かどうかを
# どのように確認するか。

# もちろん、全ての組み合わせをチェックすれば時間が足りない。
# そこで、逆に公約数側を動かし、数列の中にその倍数が
# いくつ含まれているかを数える……という方針でチェックする。

# その際、まずリスト nums を用意し、数列に含まれる数 i に
# ついて、nums[i] = 1 とする。
# あとは、エラトステネスの篩の要領で、ある数の倍数の場所を
# 順番にチェックしつつ値を合計したものが、数列の中に含まれる
# ある数の倍数の数、ということになる。

# この計算量は、O(N/2 + N/3 + N/4 + ...) = O(N logN) で
# 十分間に合う。

from math import gcd
from functools import reduce
def main():
    N = int(input())
    A = list(map(int, input().split()))

    # とりあえず全ての数の最大公約数をチェック
    all_gcd = reduce(gcd, A)
    if all_gcd != 1:
        print('not coprime')
        return

    # 一応上限を出しておく。10**6 + 1 で決め打ってもいい。
    limit = max(A) + 1

    # 数の存在チェックリスト
    nums = [0] * limit
    for a in A:
        nums[a] = 1

    # エラトステネスの篩に近い要領で、
    # 各数字の倍数の数を数えていく。
    for i in range(2, limit):
        cnt = sum(nums[i::i])
        if cnt > 1:
            print('setwise coprime')
            return
    else:
        print('pairwise coprime')

main()


