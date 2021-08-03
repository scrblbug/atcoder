# AtCoder Beginner Contest 031 C - 数列ゲーム
# https://atcoder.jp/contests/abc031/tasks/abc031_c
# tag: 数列 連続部分列 累積和 ゲーム 二人ゲーム 高橋君 青木君

# 考察を行ってもいいが、制約が 1 <= N <= 50 と緩いので
# 何も考えず全探索するのが楽で早い。

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # あらかじめ累積和を奇数・偶数番目のもので取っておく。
    # 実際には制約が緩いので、累積和を使用する必要はない。
    # まあ練習と思って……
    csum = [0, 0]
    for i, a in enumerate(A):
        csum.append(csum[i] + a)

    result = -10**10

    # t_pos: 高橋君の選ぶ場所
    # a_pos: 青木君の選ぶ場所 として全探索。
    for t_pos in range(N):
        tak_final_score = 0
        aok_max_score = -10**10
        for a_pos in range(N):
            if t_pos == a_pos:
                continue

            # 使用する数列の範囲。
            left, right = min(t_pos, a_pos), max(t_pos, a_pos)

            tak_left, aok_left = left, left + 1

            # 選んだ長さによって、右端をどちらが取るかは変わる。
            if (right - left) % 2 == 0:
                tak_right, aok_right = right, right - 1
            else:
                aok_right, tak_right = right, right - 1

            # 累積和を用いて点数を計算
            tak_score = csum[tak_right+2] - csum[tak_left]
            aok_score = csum[aok_right+2] - csum[aok_left]

            # 青木君のスコアが最大になるところが、高橋君のスコア。
            if aok_score > aok_max_score:
                aok_max_score = aok_score
                tak_final_score = tak_score

        # 高橋君のスコアが確定したら、今までの最大値と比較する。
        if result < tak_final_score:
            result = tak_final_score

    print(result)

main()
