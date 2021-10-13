# AtCoder Beginner Contest 125 C - GCD on Blackboard
# https://atcoder.jp/contests/abc125/tasks/abc125_c
# tag: 整数 最大公約数 累積和

# 数列を、A[0] ～ A[N-1] へ格納する。

# A[i] を書き換えると仮定したとき、
# A[0] ～ A[i-1] の最大公約数 g と、
# A[i+1] ～ A[N-1] の最大公約数 h を求める。
# A[i] は、g と h の最大公約数に書き換えるのが
# 最もいい書き換え方になる。

# ということを踏まえると、実は A[i] は書き換えるのではなく
# 単に消してしまっても結果は同じになる。

# つまり、数列のうちからひとつ数字を消したときの、
# 残りの最大公約数を最大化する、という問題になる。

# これは、左右から累積和のようにして最大公約数を取っておき、
# その左右の累積和を組み合わせることにより、それぞれ O(1) 
# で求めることができるようになる。

import math
def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 左からの累積最大公約数
    csum_left = [A[0]]
    for a in A[1:]:
        csum_left.append(math.gcd(csum_left[-1], a))

    # 右からの累積最大公約数
    csum_right = [A[-1]]
    for a in A[N-2::-1]:
        csum_right.append(math.gcd(csum_right[-1], a))

    result = 1

    # A[i] を消したときの最大公約数を全通り、
    # 左右からの累積を利用して求める。
    for i in range(N):
        if i == 0:
            tmp_gcd = csum_right[N-2]
        elif i == N-1:
            tmp_gcd = csum_left[N-2]
        else:
            left = i - 1
            right = N - 2 - i
            tmp_gcd = math.gcd(csum_left[left], csum_right[right])

        if tmp_gcd > result:
            result = tmp_gcd

    print(result)

main()

