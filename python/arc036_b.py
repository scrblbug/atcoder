# AtCoder Regular Contest 036 B - 山のデータ
# https://atcoder.jp/contests/arc036/tasks/arc036_b
# tag: 数列 考察

# 高さの等しい地点は存在しないので、
# 数列は必ず連続増加→連続減少を繰り返す形になる。
# （連続数は 1 以上とする）

# つまり、
# ...(増加, 減少), (増加, 減少), ....
# となっていると考えれば、数列全体を山が連続しているものと
# みなすことが出来る。

# 山の境界条件は、数列の両端と、減少→増加と転じているところ。

def main():
    N = int(input())
    field = [int(input()) for _ in range(N)]

    result = 0

    # N <= 2 ならそのまま返す。
    if N <= 2:
        print(N)
        return

    # 境界を確認していく。
    borders = [0]
    for i in range(1, N-1):
        if field[i-1] > field[i] < field[i+1]:
            borders.append(i)
    borders.append(N-1)

    # 求めた境界を元に、各山の幅を求めていく。
    result = 0
    for i in range(len(borders)-1):
        width = borders[i+1] - borders[i] + 1
        if result < width:
            result = width

    print(result)

main()
