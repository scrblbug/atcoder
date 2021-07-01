# AtCoder Beginner Contest 112 D - Partition
# https://atcoder.jp/contests/abc112/tasks/abc112_d
# tag: 整数 最大公約数 約数列挙

# M は求める最大公約数で割り切れる必要がある。
# そこで、M のある約数を d とすると、
# 作成される数列は、全て d で割り切れる必要がある。
# よって、数列の合計は d * N 以上でなければならない。
# つまり、M >= d * N を満たす最大の d が答えとなる。

def main():
    N, M = map(int, input().split())

    # 約数列挙
    divisors = set()
    for d in range(1, int(M**0.5) + 1):
        if M % d == 0:
            divisors.add(d)
            divisors.add(M // d)

    # 昇順にソートしておく
    divisors = sorted(list(divisors))

    result = 1

    # 小さいものから順に、条件を満たすかどうかを確認
    for d in divisors:
        if M >= d * N:
            result = d
        # 条件を満たさなくなれば打ち切る
        else:
            break
    
    print(result)

main()
