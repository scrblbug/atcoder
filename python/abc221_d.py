# AtCoder Beginner Contest 221 D - Online games
# https://atcoder.jp/contests/abc221/tasks/abc221_d
# tag: 座標圧縮 いもす法 典型問題 高橋君

# いもす法と呼ばれる手法で解く。

# A B で表されるプレイヤーがいる場合、人数の変化に着目すると
# A 日目の変化は +1、A+B 日目の変化は -1 となる。

# 日付ごとの変化量を記録するリストを用意しておき、
# 上記の変化をまとめていくことで、日付ごとの
# 人数の変化を作成することが可能。

# 今度は逆に日付ごとに順番に見ていき、現在の人数に
# 人数の変化を加えることで、その日付に何人いるのかを
# 把握することができる。

# 入力例 1 でいうと、作成される変化のリストは
# [0, 1, 1, 0, -1, -1] となり、その累積和
#  0, 1, 2, 2, 1, 0 が、実際の人数となる。

# のだが、日付の制約が緩く、全ての日付分の
# リストを作成すると TLE になってしまう。

# よって、まず日付を座標圧縮した後、いもす法を
# 用いる形で解く

def main():
    N = int(input())
    players = [list(map(int, input().split())) for _ in range(N)]

    # 座標圧縮の準備。全ての座標をリストにする。
    day_list = []
    for a, b in players:
        day_list.append(a)
        day_list.append(a + b)

    # 重複をなくし、ソートする。
    # 圧縮後 → 圧縮前が day_list[i] で求まるようになる。
    day_list = list(set(day_list))
    day_list.sort()

    # 圧縮前 → 圧縮後が comp_dic[day] で求まるよう、辞書を作成。
    comp_dic = {day:i for i, day in enumerate(day_list)}

    # 圧縮後の座標を利用して、いもす法を行う。
    imos = [0] * len(day_list)
    for a, b in players:
        imos[comp_dic[a]] += 1
        imos[comp_dic[a + b]] -= 1

    result = [0] * (N+1)

    # いもす法で人数と経過した日数を求めていく。
    num = 0
    prev_day = 0
    for i in range(len(day_list)):
        now = day_list[i]
        result[num] += now - prev_day

        num += imos[i]
        prev_day = now

    print(*result[1:])

main()
