# AtCoder Regular Contest 114 A - Not coprime
# https://atcoder.jp/contests/arc114/tasks/arc114_a
# tag: 素数 素因数分解 bit全探索

# それぞれの X を構成している素因数を確認する。
# 求める数は、全ての X と最低一つ共通の素因数を
# 持っている数、ということになる。
# そこで、そのような数をすべて求めてやり、
# その中で最小のものを探す。

def main():
    N = int(input())
    X = list(map(int, input().split()))

    # 50までの素数を列挙しておく
    # ここではエラトステネスの篩を使っているが、使うほどでもない
    primep = [True] * 50
    primep[0], primep[1] = False, False
    for i in range(2, 50):
        if primep[i] == True:
            for j in range(2*i, 50, i):
                primep[j] = False
    primes = [n for n in range(50) if primep[n]==True]

    # set()で管理してもいいが、ここでは後で用いるbit探索と
    # 相性がいいように、それぞれの X がどの素因数を使用しているかを
    # ビットで管理しておくようにした
    x_prime_bit = []
    for x in X:
        p_bit = 0
        for i, p in enumerate(primes):
            if x % p == 0:
                p_bit += 1<<i
        x_prime_bit.append(p_bit)
    
    # ビット全探索で、全ての素数の組み合わせを試していく
    # st: 今確認中のビット列
    result = 10**18
    for st in range(1<<len(primes)):
        # xb: 個々の X の素因数をビット列で表したもの
        # st & xb はビット演算。最低一つは共通のビットを持つ
        # ＝共通の素数を使用しているかどうかを確認している
        if all(st & xb for xb in x_prime_bit):
            # 全ての X と最低一つの共通の素数を持っているなら、
            # 改めて素数を掛け合わせていき、実際の数を確認・比較する
            tmp_r = 1
            for i in range(len(primes)):
                if 1<<i & st:
                    tmp_r *= primes[i]
            if tmp_r < result:
                result = tmp_r
    
    print(result)

main()

