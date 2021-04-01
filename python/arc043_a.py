# AtCoder Regular Contest 043 A - 点数変換
# https://atcoder.jp/contests/arc043/tasks/arc043_a
# tag: 考察 コーナーケース

# P, Q それぞれについて、A, B がどのように変動するのかを考える。
# P を動かした場合、全ての点数が P 倍される。
# つまり、平均値・最大値 - 最小値はそれぞれ P 倍されることになる。
# Q を動かした場合には、平均値は丁度 +Q され、最大値 - 最小値は変動しない。

# そこで、方針としてはまず P によって B を合わせてから、
# Q によって A を合わせることになる。

def main():
    N, A, B = map(int, input().split())
    scores = [int(input()) for _ in range(N)]

    # あらかじめ (最大値 - 最小値) と平均値を求めておく
    diff = max(scores) - min(scores)
    average = sum(scores) / N

    # 最大値 = 最小値 のとき、つまり点数が一種類しかない場合は、
    # 最大値 - 最小値 を 0 以外にはできない。
    if diff == 0 and B != 0:
        print(-1)
        return
    # (最大値 - 最小値) = A = 0 の時は、便宜的に P = 1 としていい
    elif diff == 0:
        P = 1
    # それ以外の場合は、P を普通に計算する
    else:
        P = B / diff

    Q = A - average * P

    print(P, Q)

main()
