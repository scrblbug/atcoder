# AtCoder Regular Contest 067 C - Factors of Factorial
# https://atcoder.jp/contests/arc067/tasks/arc067_a
# tag: 整数 約数 素因数分解 数え上げ MOD

# N! の約数の個数をそのまま列挙していっては間に合わない。
# 約数の数さえ分かればいいので、効率よく数える方法を
# 考える。

# 例えば 4! を考えると、4! = 24 で、その約数は
# 1, 2, 3, 4, 6, 8, 12, 24 の 8 個。
# ところで、24 を素因数分解すると、
# 2^3 * 3 になる。
# 約数は、この各素因数をいくつずつ掛けるかによって
# 求めることが出来る。
# f.e. 4 = 2^2 * 3^0, 12 = 2^2 * 3^1, 1 = 2^0 * 3^0
# つまり、24 の約数は 2 ^(0～3) * 3^(0～1) によって
# 網羅され、その個数は 2 と 3 をそれぞれ何回掛けるかの
# 組み合わせ数、つまり 0～3 の 4 通り掛ける 0～1 の 2通り
# で 4 * 2 = 8 通り となる。

# 以上のことより、素因数の組み合わせとそれぞれの個数の
# 最大数を求めることができれば、答えを出すことが出来る。

# これは、階乗の定義から、1～N のそれぞれを素因数分解し、
# 数を数えていくことで求めることが出来る。
# つまり、4! = 1 * 2 * 3 * 4
# = 1 * (2^1) * (3^1) * (2^2)
# = 1 * (2^3) * (3^1)

from collections import Counter
def main():
    N = int(input())
    MOD = 10**9 + 7

    # エラトステネスのふるいであらかじめ素数を列挙
    primep = [True] * (N+1)
    primep[0], primep[1] = False, False
    for i in range(N+1):
        if primep[i] == False:
            continue
        for j in range(2*i, N+1, i):
            primep[j] = False
    primes = [n for n in range(N+1) if primep[n]]

    # 素因数分解用に関数を作っておく
    # 渡された数を素因数分解し、{素因数: 個数} の
    # 辞書を返す。
    def prime_factorization(num):
        result = Counter()

        # 素数で割り切れるかどうかを確認していく
        for p in primes:
            # この問題は制約が緩いので最後まで調べてもいいが、
            # 調べるのは num**0.5 まででいい。
            if p > num ** 0.5:
                break

            # 同じ素数で割れる間は割り続ける
            while num % p == 0:
                result[p] += 1
                num //= p

        # 1 より大きな数字が残っていれば、それは素数になる
        if num != 1:
            result[num] += 1

        return result

    # 1 ～ N+1 のそれぞれを素因数分解し、
    # 全体の素因数とその個数を求める
    p_cnt = Counter()
    for i in range(1, N+1):
        p_cnt += prime_factorization(i)

    # 答えは、それぞれの (素因数の数 + 1) を掛け合わせた
    # ものになる。（選ばない場合も含むため）
    result = 1
    for c in p_cnt.values():
        result = (result * (c+1)) % MOD

    print(result)

main()
