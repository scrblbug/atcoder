# AtCoder Beginner Contest 142 D - Disjoint Set of Common Divisors
# https://atcoder.jp/contests/abc142/tasks/abc142_d
# tag: 整数 公約数 素数 素因数分解 考察 素数列挙 最大公約数 エラトステネスの篩

# まず、知っていると便利な事柄としては、ある二つの整数 A, B の
# 公約数は、A, B の最大公約数の約数である。

# さて、全てが互いに素の組み合わせを考える時、結論から言うと
# 全ての公約数のうち、素数（と 1 ）の集合が、最大の個数となる。
# 注意： 素数はほかの素数と、1 は他の全ての数と互いに素

# 逆に素数でない数、つまり合成数を含む場合には、

# 1) 合成数が素数の n 乗の場合
# これは底となる素数と入れ替えても数が変化しない

# 2) 合成数が二つ以上の素数を約数に保つ場合
# これは明らかに素数のみの集合よりも数が減ってしまう

# ことから、明らか。

# 以上をまとめると、求めるものは A, B の最大公約数を
# 素因数分解し、得られた素数と 1 の集合の要素数ということになる。

# エラトステネスの篩で素数列挙
def get_prime_list(limit):
    if limit < 2:
        return []
    primep = [True] * (limit+1)

    # 3以上の奇数のみを順番に見ていく
    for n in range(3, int(limit ** 0.5) + 1 , 2):
        if primep[n] == True:
            # 素数の奇数倍のみ書き換えすればOK
            for i in range(n * 3, limit + 1, n * 2):
                primep[i] = False
    return [2] + [p for p in range(3, limit+1, 2) if primep[p]==True]

# 素因数分解
def prime_factorize(n):
    # まずは、使用する素数を列挙しておく（n の平方根まで）
    primes = get_prime_list(int(n**0.5))

    result = []

    # n を素数で割っていくのを順番に試す
    for p in primes:

        # n が素数で割り切れるなら、指数を求めて答えに格納
        power = 0
        if n % p == 0:
            while n % p == 0:
                power += 1
                n //= p
            result.append((p, power))

    # 最後に n が 1 になってなければ、素数が残っている
    if n > 1:
        result.append((n, 1))

    return result

# 最大公約数
# もちろん math.gcd でもいいけど、せっかくなので……
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# ここから main()
def main():
    A, B = map(int, input().split())

    # 最大公約数を求め、素因数分解し、要素数に +1 したものが答え
    g = gcd(A, B)
    pf = prime_factorize(g)
    print(len(pf)+1)

main()