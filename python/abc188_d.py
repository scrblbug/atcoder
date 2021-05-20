# AtCoder Beginner Contest 188 D - Snuke Prime
# https://atcoder.jp/contests/abc188/tasks/abc188_d
# tag: 高橋君 座標圧縮 いもす法 株式会社すぬけ

# ひとまず、すぬけプライムを使用しなかった場合に
# 費用をどのように求めるのかを考えてみる。
# 制約が 1 <= a, b <= 10^9 となっているので、一日一日を
# 真面目に計算していては、間に合わなくなる。
# つまり、費用が変化するときだけに注目し、その間については
# 日数を掛けて求めるという方針になる。

# すぬけプライムについては、上記に加えて料金に上限を
# 設けることを考えるだけで良い。

from collections import defaultdict
def main():
    N, prime_cost = map(int, input().split())
    services = [list(map(int, input().split())) for _ in range(N)]

    changes = defaultdict(int)

    # サービスごとに a 日目に始まり、b 日目に終わる。つまり、
    # a 日目に全体の費用は c 上がり、b+1 日目に c 下がることになる
    for a, b, c in services:
        changes[a] += c
        changes[b+1] -= c

    # 変更の起こる日にちだけを抜き出し、ソートする（座標圧縮）
    t_list = list(changes.keys())
    t_list.sort()

    result = 0

    # 現在の（すぬけプライムを除く）一日あたりの費用
    cost = 0

    # 前回変動の起こった日にち
    prev_t = 0

    # 日にち順に費用を計算する
    for t in t_list:
        # 前回の変動日～今までの費用を求める
        # すぬけプライムを一日あたりの費用の上限とする
        result += (t - prev_t) * min(cost, prime_cost)
        cost += changes[t]
        prev_t = t

    print(result)

main()


