# AtCoder Regular Contest 100 C - Linear Approximation
# https://atcoder.jp/contests/arc100/tasks/arc100_a
# tag: 数列 マンハッタン距離 最小値 事前変形 中央値

# 引かれる数が 1ずつ増えていくので、あらかじめ
# 引いておいた数列を作成しておく。

# すると、ある数列に対して距離の差分の合計が
# もっとも小さくなる一点を求める、という問題に帰着される。

# これはマンハッタン距離の差分の最小値なので、
# 中央値を求めればいい。

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # a, a-1, a-2 ... を作成
    converted = [a - i for i, a in enumerate(A)]

    # 中央値
    med = sorted(converted)[N//2]

    # 回答
    print(sum(abs(n - med) for n in converted))

main()
