# AtCoder Beginner Contest D - Disjoint Set of Common Divisors
# https://atcoder.jp/contests/abc142/tasks/abc142_d
# tag: 公約数 素数 素因数分解 考察

# まず、知っていると便利な事柄としては、ある二つの整数 A, B の
# 公約数は、A, B の最大公約数の約数である。

# さて、全てが互いに素の組み合わせを考える時、結論から言うと
# 全ての公約数のうち、素数（と 1 ）の集合が、最大の個数となる。

# 逆に素数でない数、つまり合成数を含む場合には、

# 1) 合成数が素数の n 乗の場合
# これは底となる素数と入れ替えても数が変化しない

# 2) 合成数が二つ以上の素数を約数に保つ場合
# これは明らかに素数のみの集合よりも数が減ってしまう

# ことから、明らか。

# 以上をまとめると、求めるものは A, B の最大公約数を
# 素因数分解し、得られる素数と 1 の集合、ということになる。

# エラトステネスの篩
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
def prime_factorization(n):
    primes = get_prime_list(int(n**0.5))
    result = []
    for p in primes:
        if p >= n:
            break
        power = 0
        if n % p == 0:
            while n % p == 0:
                power += 1
                n //= p
            result.append((p, power))
    if n > 1:
        result.append((n, 1))
    return result

# 最大公約数
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def main():
    A, B = map(int, input().split())
    g = gcd(A, B)

    pf = prime_factorization(g)
    print(len(pf)+1)

main()