def main():
    W, H = map(int, input().split())
    # W, H <= 10**5 なので、通常のO(WH)のDPでは間に合わない
    # つまり、数学的にショートカットしてやる必要がある

    # 縦に H 進む間に横に W 進む必要があると、
    # 縦横を独立すると考えた場合、
    # 縦横縦縦横 ……のように、縦（H個）横（W個）の列の
    # 組み合わせの個数、ということになる

    # この組み合わせの個数は、最終的に
    # (W+H)! / W!H!にて計算可能
    # （一緒くたに並べて、縦横それぞれ同士を区別しないようにする）

    MOD = 10**9 + 7

    # 以下いろいろと事前計算しておく
    # 階乗
    fact = [1]
    for i in range(1, 10**5 * 2 + 1):
        fact.append((fact[-1] * i) % MOD)

    # 逆元
    # P = qa + r 、aの逆元をA、rの逆元をRとおく（以下mod P）
    # qa + r = 0
    # r = -qa
    # rRA = -qaAR   （両辺にARを掛ける）
    # A = -qR       （rR = 1, aA = 1より）
    inv = [1, 1]
    for i in range(2, 10**5+1):
        inv.append((-(MOD // i) * inv[MOD % i]) % MOD)
    
    # 逆元の階乗
    fact_inv = [1, 1]
    for i in range(2, 10**5+1):
        fact_inv.append((fact_inv[-1] * inv[i]) % MOD)

    # 進む歩数は実際にはW-1, H-1歩
    W -= 1
    H -= 1
    
    result = (fact[W+H] * fact_inv[W] * fact_inv[H]) % MOD
    print(result)

main()
