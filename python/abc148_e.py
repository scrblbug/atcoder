# AtCoder Beginner Contest 148 E - Double Factorial
# https://atcoder.jp/contests/abc148/tasks/abc148_e
# tag: 発想力

# 一つ飛ばしの階乗を考えた時の末尾の 0 を数える……
# といった問題。

# まず、末尾に 0 が付くためには、少なくとも 2 の倍数と
# 5 の倍数が含まれる必要がある。

# ここで、N が奇数だとすると、f(N) は奇数のみを掛け合わせた
# 数になるので、2 の倍数を含むことはない。つまり、0 が
# 末尾につくことはない。

# よって、N が偶数の場合のみ考えればいい。この場合、
# 掛けられる全ての数は 2 の倍数なので、5 の倍数のみ
# 考えれば良い。

# 数字を順番に見ていくと 2, 4, 6, 8, 10, 12, ...
# であり、5 の倍数は 5, 10, 15 番目ということになる。
# また、25番目の数、50 には因数として 5 が 2 個
# 含まれることになる……といったことをふまえると、

# つまり、掛けられる数字の個数 (N / 2) までの数字に、
# 5 の倍数、25 の倍数、125 の倍数……がいくつあるのかを
# 数えればいい、ということになる。

def main():
    N = int(input())
    if N % 2 == 1:
        print(0)
        return
    
    # 数字の個数に変換
    N //= 2

    # 除数、答えの初期化
    divisor = 5
    result = 0

    # 5, 25, 125... で割った数を答えに足していく
    while divisor <= N:
        result += N // divisor
        divisor *= 5
    
    print(result)

main()
