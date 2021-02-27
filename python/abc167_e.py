# AtCoder Beginner Contest 167 E - Colorful Blocks
# https://atcoder.jp/contests/abc167/tasks/abc167_e
# tag: 順列組み合わせ 階乗 逆元 MOD

# DPだと間に合わない。
# 隣り合うブロックの組であって同じ色で塗られている組の数
# ＝左隣と同じ色のブロックの数、と考えても良い（右でもどっちでもいい）

# つまり、隣と同じ色の組数を k として固定すると、
# 左端を除く N-1 個のブロックのうちから左隣と同じ色にする
# ブロックを k 個選ぶ、と言い換えることもできる
# この組み合わせは (N-1)! / (N-1-k)!k! となる
# それ以外の N - k 個のブロックは、左端のブロックを除いて
# 左隣のブロックと違う色を選ぶことになる
# これは M * (M-1)^(N-k-1)
# これを、k 毎(0 <= k <= K)に足し合わせていく

def main():
    N, M, K = map(int, input().split())
    MOD = 998244353

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
    for i in range(2, 2 * 10**5 + 1):
        inv.append((-(MOD // i) * inv[MOD % i]) % MOD)
    
    # 逆元の階乗
    fact_inv = [1, 1]
    for i in range(2, 2 * 10**5 + 1):
        fact_inv.append((fact_inv[-1] * inv[i]) % MOD)

    result = 0

    for k in range(K+1):
        t1 = (fact[N-1] * fact_inv[N-1-k] * fact_inv[k]) % MOD
        t2 = (M * pow(M-1, N-k-1, MOD)) % MOD
        result = (result + (t1 * t2)) % MOD
    
    print(result)

main()
