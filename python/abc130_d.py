# AtCoder Beginner Contest 130 D - Enough Array
# https://atcoder.jp/contests/abc130/tasks/abc130_d[
# tag: 数列 部分列 数え上げ 累積和 尺取法 二分探索

# 尺取法で解くのが最速。(O(N))
# [左, 右] の区間を左を中心に考え、[0, 0] から始める。
# 以下の内容をループ。

# 現在の区間が条件を満たすまで、区間右を伸ばす。
# 条件を満たしたら、そこから右の組み合わせは全て条件を満たすので、
# その数を答えに加算し、区間左を一つ縮める。
# 区間右が右端に到達しても条件を満たせなくなる or 
# 区間左が右端を越える時に、ループを終了する。

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 区間左、区間右、現在の合計値
    left, right, now = 0, 0, A[0]
    result = 0
    while True:
        # 条件を満たすまで区間右を伸ばす
        if now < K:
            if right < N - 1:
                right += 1
                now += A[right]
            # 伸ばしきっても条件を満たせなければ、終了
            else:
                break
        # 条件を満たしているなら
        else:
            # 答えを加算
            result += N - right
            # 区間左を縮める
            if left < N - 1:
                now -= A[left]
                left += 1
                # 区間右に追いついている場合は、区間右も一つ右側にずらす
                if right < left:
                    right += 1
                    now += A[right]
            # すでに区間左が右端に到達していれば、終了
            else:
                break

    print(result)

main()

# 尺取法を使わなくても、それぞれの区間左に対する区間右を
# 二分探索で求め、回答することも可能。(O(N logN))
# その場合は、合計値を素早く求めるために、あらかじめ累積和を
# 取っておく。

# 二分探索は実装してもいいが、今回のように単純なものなら
# ライブラリ bisect を使うと早い。

from bisect import bisect_left
def main2():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 累積和を取っておく
    csum = [0]
    for a in A:
        csum.append(csum[-1] + a)

    result = 0
    for left in range(N):
        sum_left = csum[left]
        sum_right_need = K + sum_left

        # bisect による二分探索で、区間右の場所を求める
        right = bisect_left(csum, sum_right_need)

        # csum の最初に 0 を入れたため bisect の値も 1 ずれているので注意。
        result += N - right + 1

    print(result)

# main2()
