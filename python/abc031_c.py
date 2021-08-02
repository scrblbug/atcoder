# AtCoder Beginner Contest 031 C - 数列ゲーム
# https://atcoder.jp/contests/abc031/tasks/abc031_c
# tag: 数列 連続部分列 ゲーム 二人ゲーム 高橋君 青木君

# 考察を行ってもいいが、制約が 1 <= N <= 50 と緩いので
# 何も考えず全探索するのが楽で早い。

def main():
    N = int(input())
    A = list(map(int, input().split()))

    result = -10**10

    # t_pos: 高橋君の選ぶ場所
    # a_pos: 青木君の選ぶ場所 として全探索。
    for t_pos in range(N):
        a_max_score = -10**10
        for a_pos in range(N):
            if t_pos == a_pos:
                continue

            # 数列を取り出す。
            left, right = min(t_pos, a_pos), max(t_pos, a_pos)
            ext = A[left:right+1]

            # それぞれのスコア。
            # 制約が厳しい場合は、ここで累積和などを用いる。
            t_score = sum(ext[::2])
            a_score = sum(ext[1::2])

            # 青木君の最高スコアが更新された時に、その時の
            # 高橋君のスコアを記録しておく。
            if a_score > a_max_score:
                a_max_score = a_score
                t_score_final = t_score

        if result < t_score_final:
            result = t_score_final

    print(result)

main()
