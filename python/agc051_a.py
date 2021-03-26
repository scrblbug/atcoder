# AtCoder Grand Contest 051 A - Dodecagon
# https://atcoder.jp/contests/agc051/tasks/agc051_a
# tag: 考察

# 外から敷き詰めていくことを考えると、角以外の部分では同じ図形を
# 並べ、角の部分で正方形と正三角形を組み合わせる形になる。
# その結果、正三角形を並べたところは、内側の辺の長さが 1 減る
# ことになる。

# つまり、あるタイミングで辺の長さが2種類の (a, b) 十二角形
# になった時、次回の遷移は (a-1, b) もしくは (a, b-1) の
# 十二角形である。

# どちらの辺に対して三角形（正方形）を適用するかで、二通りに
# 別れていくことになる。

# この調子で行くと、いつか辺の長さのうちどちらかが 0 になるが、
# それ以降は正六角形になるため、敷き詰め方が正三角形による一種類に
# 限定されるようになる。

# 試しに d = 1, 2 の場合の遷移を考えてみると、

# d = 1:
# (1, 1) → (0, 1)
#        → (1, 0)

# d = 2:
# (2, 2) → (1, 2) → (0, 2)
#                 → (1, 1) → (0, 1)
#                          → (1, 0)
#        → (2, 1) → (2, 0)
#                 → (1, 1) → (0, 1)
#                          → (1, 0)

# この通り数は、初期値 (0, 0) のどちらかに 1 ずつ加えていき、
# (d, d) に変化させる通り数ということになり、つまりは 2d C d
# ということになる。（もちろん、これは二項係数の中央項でもある）

# ただし、初期値 (d, d) では両辺を区別しない（＝回せば同じ図形）
# ので、実際の数は 1/2 になる。

def main():
    d = int(input())
    MOD = 998244353

    # 階乗・及び逆元の階乗を求めておく（いつもの）
    fact = [1]
    for i in range(1, 2*d + 1):
        fact.append((fact[-1] * i) % MOD)
    
    inv = [1, 1]
    for i in range(2, d+1):
        inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    
    inv_fact = [1]
    for i in range(1, d+1):
        inv_fact.append((inv[i] * inv_fact[-1]) % MOD)

    # n C r = n! // ((n-r)! * r!)
    # ついでに 2 の逆元も掛けておく
    result = ((fact[2 * d] * inv_fact[d] * inv_fact[d] * pow(2, -1, MOD)) % MOD) 
    print(result)

main()