# diverta 2019 Programming Contest D - DivRem Number
# https://atcoder.jp/contests/diverta2019/tasks/diverta2019_d
# tag: 整数 約数 約数列挙

# 商と余りを x としてみる。
# m がお気に入りの数とすると、
# mx + x = N
# x(m+1) = N
# つまり、m+1 は N の約数である必要がある。

# そこで、あらかじめ N の約数を列挙しておき、
# 1 引いた数が条件を満たすかどうかを確認していく。

def main():
    N = int(input())

    divisors = []

    # 約数全列挙
    for d in range(1, int(N**0.5)+1):
        if N % d == 0:
            divisors.append(d)
        if d**2 != N:
            divisors.append(N//d)

    result = 0
    for d in divisors:
        # 条件を満たせば答えに足す
        m = d - 1
        if m == 0:
            continue
        if N // m == N % m:
            result += m
    
    print(result)

main()
