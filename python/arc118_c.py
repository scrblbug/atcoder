# AtCoder Regular Contest 118 C - Coprime Set
# https://atcoder.jp/contests/arc118/tasks/arc118_c
# 整数 最大公約数 素数 考察

# 各数の素因数を考える。
# 仮に N = 3 のとき、素因数の種類を A, B, C とすると、
# B*C, C*A, A*B の時に条件を満たす。
# また、ここに D*B*C, E*C*A などを追加しても、
# 条件を満たしたまま。（D, E は2以上の任意の整数）

# 仮に A, B, C = [2, 3, 5] とすると、
# [6, 10 ,15] を得ることが出来る。
# ところで、1 <= Ai <= 10000 という制限がある。
# ここに、10000以下の6 の倍数と10の倍数と15の倍数を
# 加えていけば制限内で N = 2500 を達成可能。（全部で2666個）

def main():
    N = int(input())
    result = [6, 10, 15]

    # 6 の倍数を追加
    i = 2
    while 6 * i <= 10000:
        result.append(6 * i)
        i += 1
    print(len(result))

    # 10 の倍数を追加
    i = 2
    while 10 * i <= 10000:
        # 30 の倍数は 6 の倍数と重複するので外す
        if 10 * i % 30 != 0:
            result.append(10 * i)
        i += 1
    print(len(result))

    # 15 の倍数を追加
    i = 2
    while 15 * i <= 10000:
        # 同様
        if 15 * i % 30 != 0:
            result.append(15 * i)
        i += 1
    print(len(result))

    print(*result[:N])

main()
