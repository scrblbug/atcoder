# AtCoder Regular Contest 127 A - Leading 1s
# https://atcoder.jp/contests/arc127/tasks/arc127_a
# tag: 整数 考察

# f(N) の値に従って分類する、つまり先頭から 1 が 
# 1 個だけ並んでいる数、2 個だけ並んでいる数……
# と考えるとややこしくなるので、一般化を考える。

# 具体的に、111 という数について考えてみると、
# f(111) = 3 となるが、これを
# 1** に対して +1、11* に対して +1、111 に対して +1 と
# 考えることも可能。

# すなわち、
# 1 で始まる数の個数 +
# 11 で始まる数の個数 + 
# 111 で始まる数の個数 +
# ....

# が、回答と等しくなる。

# 1 で始まる数とは、
# 1 桁: 1
# 2 桁: 10～19
# 3 桁: 100～199
# 4 桁: 1000～1999

# 11 で始まる数なら、
# 1 桁: 無し
# 2 桁: 11
# 3 桁: 110～119
# 4 桁: 1100～1199

# この下限(bottom)の推移と上限(top)の推移に注目すると、
# 次の範囲を簡単に数式で表せそうである。

# 以上を踏まえながら、回答を実装していく。
def main():
    N = int(input())

    result = 0
    # 1 が先頭から i 個続いている数の個数を数えていく。
    for i in range(1, 16):
        # 最初の数を構築
        start = int('1' * i)
        if start > N:
            break
        else:
            result += 1
        bottom = top = start

        # 桁を上げながら、数えていく。
        while True:
            # top と bottom を次の桁数用に更新する。
            bottom *= 10
            top = (top + 1) * 10 - 1

            # 範囲が含まれなくなったら break。
            if N < bottom:
                break

            # 含まれている範囲を数える。
            result += min(N, top) - bottom + 1

    print(result)

main()
