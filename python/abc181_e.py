# AtCoder Beginner Contest 181 E - Transformable Teacher
# https://atcoder.jp/contests/abc181/tasks/abc181_e
# tag: 累積和 考察

# 先生を入れた全体でいうと、身長順に並び替えた後、順番に
# 二人ずつペアにしていくのが最善。

# 生徒が 5 人の場合で考えてみる。
# ソート済みの生徒の身長を a, b, c, d, e、先生の身長を T とすると、
# 先生を入れてソートし直すと、次のパターンが考えられる。

# 1) T, a, b, c, d, e
# 2) a, T, b, c, d, e
# 3) a, b, T, c, d, e
# 4) a, b, c, T, d, e
# 5) a, b, c, d, T, e
# 6) a, b, c, d, e, T

# 身長差の和を考えたときは、1)と2)、3)と4)、5)と6)は
# まとめてしまっていい。つまり、

# 1) T, a, b, c, d, e  ans: |T-a| + |b-c| + |d-e|
# 2) a, b, T, c, d, e  ans: |a-b| + |T-c| + |d-e|
# 3) a, b, c, d, T, e  ans: |a-b| + |c-d| + |T-e|

# 先生は、かならず奇数番目の生徒とペアになることになる。
# また、先生のペアより手前の生徒は (2n+1番目, 2n+2番目) のペアとなり、
# 先生のペアより後の生徒は (2n番目, 2n+1番目) のペアとなることが分かる。

# ということは、あらかじめ (a, b), (c, d)...とペアにしたときの
# 差分の累積和と、(b, c), (d, e)...とペアにしたときの累積和を
# 求めておき、先生がどこに挿入されるかによって、その前後の
# 身長の差分の和を素早く求めるようにすればいい。

from bisect import bisect
def main():
    N, M = map(int, input().split())
    height = list(map(int, input().split()))
    teacher = list(map(int, input().split()))

    height.sort()

    # (a, b), (c, d)...とペアにするときの累積和。
    csum_left = [0]
    for i in range(N//2):
        csum_left.append(csum_left[-1] + abs(height[2*i]-height[2*i+1]))
    
    # (b, c), (d, e)...とペアにするときの累積和。ただし右から計算しておく。
    csum_right = [0]
    rev = list(reversed(height))
    for i in range(N//2):
        csum_right.append(csum_right[-1] + abs(rev[2*i] - rev[2*i+1]))

    result = 10**15

    # 先生の身長を全探索する。
    for th in teacher:
        # 先生とペアになる生徒のインデックスを求める。
        idx = bisect(height, th)
        if idx % 2 == 0:
            t_paired = idx
        else:
            t_paired = idx - 1
        
        # 先生の左側の生徒のみによるペア数。
        pair_left = t_paired // 2

        # 生徒のみでののペア数は (N-1) // 2 となるので、
        # 左から pair_left 組のペアが作成され、次に先生のペアが入った場合、
        # 右からは (N-1) // 2 - pair_left 組のペアとなる。
        pair_right = (N-1) // 2 - pair_left

        # 以上を元に、先生の身長が th のときの値を求め、
        # 他の結果と比較する。
        diff = csum_left[pair_left] + abs(th - height[t_paired]) + csum_right[pair_right]
        if result > diff:
            result = diff

    print(result)

main()
