# AtCoder Beginner Contest 156 D - Bouquet
# https://atcoder.jp/contests/abc156/tasks/abc156_d
# tag: 順列・組み合わせ MOD 逆元 あかりさん

# 苦手な数 a, b が無かった場合、各花を入れる・入れないの
# 2通りずつがあり、そこから空集合を除いた
# 2^n - 1 となる。

# そこから、a, b 本選んだ場合を引けば答えになる。
# つまりは、nCa と nCb を求めたい。

# ところが、2 <= n <= 10^9 と制約が厳しいので、
# よく使う nCa = n! // (a! * (n-a)!) の式だと
# 時間が掛かりすぎてしまう。

# が、a, b は比較的小さいので、地道に 
# n * (n-1) * ... * (n-a+2) * (n-a+1) // a! 
# で求めることにする。

def main():
    n, a, b = map(int, input().split())
    MOD = 10**9 + 7

    # Pythonのpowは内部的に繰り返し二乗法を使用してくれる
    result = pow(2, n, MOD) - 1

    # 逆元の階乗は求めておく
    # inv_factを作成
    t = max(a, b)
    inv = [1] * (t + 1)
    inv_fact = [1] * (t + 1)
    # aの逆元をA、q, rをp/aの商と余り、rの逆元をRとしたとき、
    # p = qa + r 両辺に A を掛けて
    # 0 = q + Ar (mod p) 両辺に R を掛けて
    # 0 = qR + A (mod p)
    # A = -qR (mod p)
    # 最初の仮定より r < a なので、下から順番に
    # 逆元を求めていくことができる。
    for i in range(2, t+1):
        inv[i] = (- (MOD // i) * inv[MOD % i]) % MOD
    for i in range(2, t+1):
        inv_fact[i] = (inv_fact[i-1] * inv[i]) % MOD

    nca = 1
    for i in range(a):
        nca = (nca * (n-i)) % MOD
    nca = (nca * inv_fact[a]) % MOD
    
    ncb = 1
    for i in range(b):
        ncb = (ncb * (n-i)) % MOD
    ncb = (ncb * inv_fact[b]) % MOD

    result = (result - nca - ncb) % MOD
    print(result)

main()