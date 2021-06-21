# AtCoder Regular Contest 066 C - Lining Up
# https://atcoder.jp/contests/arc066/tasks/arc066_a
# tag: 順列・組み合わせ 数え上げ MOD

# N が奇数の時は、中央の一人が 0 で、
# そこから端に向かって 2 ずつ増えていく。
# すなわち、それぞれの数字の出現数を数えると
# 0 - 1 回
# 2, 4, ..., N-1 の偶数 - 2 回
# となっていなければならない。

# 同様に N が偶数の時は、真ん中の二人が 1 で、
# そこから端に向かって 2 ずつ増えていく。
# この場合は
# 1, 3, ..., N-1 が 2 回ずつ出現する。

# 上記の条件を満たせば、並び方が存在する。
# 通り数については同じ数字をもつ二人を
# 独立に入れ替えられるので、2^(N//2) 通りになる。

from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    cnt = Counter(A)

    # N が奇数の場合
    if N % 2 == 1:
        if cnt[0] != 1:
            print(0)
            return
        for i in range(2, N, 2):
            if cnt[i] != 2:
                print(0)
                return

    # N が偶数の場合
    else:
        for i in range(1, N, 2):
            if cnt[i] != 2:
                print(0)
                return

    # return して無ければ回答
    print(pow(2, N//2, MOD))

main()
