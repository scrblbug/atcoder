# AtCoder Beginner Contest 144 E - Gluttony
# https://atcoder.jp/contests/abc144/tasks/abc144_e
# tag: 二分探索

# 消化コストが高い順に、食べやすいものを担当する
# 修行による変化についても、食べにくいものを担当している方が
# 最終的には、食べやすいものを担当している方以下の
# 消化コストにする必要があるので、そのまま考えていい。

# K <= 10**18 と巨大なので、修行のやり方そのものを
# 考えるのは難しい。
# 一方、時間を固定してやれば、どれくらい修行を行う
# 必要があるのかについては簡単に計算できる
# つまり、かかる最大時間を変化させる二分探索で解いていく。

import math
def main():
    N, K = map(int, input().split())
    cost = list(map(int, input().split()))
    foods = list(map(int, input().split()))

    # 担当者決め
    cost.sort()
    foods.sort(reverse=True)

    high = 10**12
    low = -1

    # 二分探索
    while high - low > 1:
        mid = (high + low) // 2

        # 必要とする修行回数を求める
        cost_diff = 0
        for c, f in zip(cost, foods):
            cost_diff += max(0, c - math.floor(mid / f))

        if cost_diff <= K:
            high = mid
        else:
            low = mid
    
    print(high)

main()
