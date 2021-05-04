# AtCoder Beginner Contest 107 C - Candles
# https://atcoder.jp/contests/abc107/tasks/arc101_a
# tag: 考察 すぬけ君

# すぬけ君を中心として、N 本のろうそくを取ることになる。
# 取る範囲の左端を決めれば、右端も決まる。
# というわけで、左端を動かして全探索する。
# このとき、0 → 左端 → 右端と動く場合と、0 → 右端 → 左端
# と動く場合の二通りを考慮する。

def main():
    N, K = map(int, input().split())
    candles = list(map(int, input().split()))

    result = 10**9

    # left: 左端のろうそくのインデックスとして全探索
    for left in range(N - K + 1):
        right = left + K - 1

        # 左端～右端の距離
        lr = abs(candles[right] - candles[left])

        # 0 → 左端 → 右端の場合
        l_first = abs(candles[left]) + lr

        # 0 → 右端 → 左端の場合
        r_first = abs(candles[right]) + lr

        # 今までの最小値の含めて比べ、一番小さいものを採用
        result = min(result, l_first, r_first)
    
    print(result)

main()
