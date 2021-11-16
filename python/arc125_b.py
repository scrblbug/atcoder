# AtCoder Regular Contest 125 B - Squares
# https://atcoder.jp/contests/arc125/tasks/arc125_b
# tag: 整数 数え上げ 平方数 MOD

# 1 <= x <= N, 1 <= y <= N
# x^2 - y は平方数

# さて、x^2 - y = s^2 になるとする。y > 0 なので、 x > s 。
# また、式変形して x^2 - s^2 = y 
# (x - s) * (x + s) = y

# x - s と x + s から x, y は確定するので、
# この組み合わせ数を考えればいい。

# x - s <= x + s なので、1 <= x - s <= sqrt(N)
# この x - s を全探索する。固定して考えると、
# (x - s) * (x + s) = y, 1 <= y <= N なので、
# x - s <= x + s <= N // (x - s)
# ただし、(x - s) + (x + s) = 2x となるから、合計は 2 で
# 割り切れる必要がある。


def main():
    N = int(input())
    MOD = 998244353

    result = 0

    # 上記考察より、x-s を i とおく。
    for i in range(1, int(N**0.5)+1):
        # x+s を j とおくと、i <= j <= N // i
        # 候補は (N//i - i + 1) 個あることになるが、
        # そのうち x-s と足して 2 で割り切れる数は、
        # (候補数 + 1) // 2 個になる。
        result = (result + ((N//i) - i + 2) // 2) % MOD

    print(result)

main()
