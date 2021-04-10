# AtCoder Beginner Contest C - Digits in Multiplication
# https://atcoder.jp/contests/abc057/tasks/abc057_c
# tag: 約数列挙 基礎問題

# N = A * B を満たす整数の組、つまり N の約数を全列挙し、
# F(A, B) の最小値を求める。
# A, B は入れ替え可能なので、仮に A <= B としておくと、
# A <= sqrt(N) となるので、探索範囲は最大 10^5 となる。

def main():
    N = int(input())

    result = 10

    # a を 1 ～ sqrt(N) の範囲で動かす
    for a in range(1, int(N**0.5) + 1):
        if N % a != 0:
            continue

        b = N // a

        # 文字列に変換した後、長さを取ることで桁数を出す
        la = len(str(a))
        lb = len(str(b))

        # 最小値を更新してるかどうかチェック
        if max(la, lb) < result:
            result = max(la, lb)

    print(result)

main()
