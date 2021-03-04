# AtCoder Beginner Contest 034 C - 経路
# https://atcoder.jp/contests/abc034/tasks/abc034_c
# tag: 順列組み合わせ MOD 階乗 逆元 

# W, H <= 10**5 なので、よくやるO(WH)のDPでは間に合わない
# つまり、数学的にショートカットしてやる必要がある

# 縦に H-1 進む間に横に W-1 進む必要があると、
# 縦横を独立すると考えた場合、
# 縦横縦縦横 ……のように、縦（H-1個）横（W-1個）の列の
# 組み合わせの個数、ということになる

# この組み合わせの個数は、最終的に
# 全部を一緒くたに並べて、縦横それぞれ同士を
# 区別しないような組み合わせの数と考えると、
# ((W-1)+(H-1))! / (W-1)!(H-1)!にて計算可能

def main():
    W, H = map(int, input().split())
    MOD = 10**9 + 7

    # 以下いろいろと事前計算しておく
    # 階乗
    fact = [1]
    for i in range(1, 2 * 10**5 + 1):
        fact.append((fact[-1] * i) % MOD)

    # 逆元
    # P = qa + r 、aの逆元をA、rの逆元をRとおく（以下mod P）
    # qa + r = 0
    # r = -qa
    # rRA = -qaAR   （両辺にARを掛ける）
    # A = -qR       （rR = 1, aA = 1より）
    inv = [1, 1]
    for i in range(2, 10**5 + 1):
        inv.append((-(MOD // i) * inv[MOD % i]) % MOD)
    
    # 逆元の階乗
    fact_inv = [1, 1]
    for i in range(2, 10**5 + 1):
        fact_inv.append((fact_inv[-1] * inv[i]) % MOD)

    result = (fact[W-1+H-1] * fact_inv[W-1] * fact_inv[H-1]) % MOD
    print(result)

main()
