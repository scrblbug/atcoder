# AtCoder Beginner Contest 156 E - Roaming
# https://atcoder.jp/contests/abc156/tasks/abc156_e
# tag: 順列・組み合わせ 数え上げ MOD

# 最終的な状態を考える。
# 人がいなくなった部屋の数を n とすると、n 人を他の
# （最終的に2人以上いる）部屋にどのように配置するのか
# という組み合わせ数と見ることが可能。

# また、ちょうど k 回というのは、途中に適当な無駄な移動を
# 挟んでやればいいので、k 回以下と読み替えてもいい。

# つまり、人がいなくなる部屋の数が 0 ～ min(k, n-1)の範囲で
# 上記の組み合わせ数を足しあわせればいい。

def main():
    # 組み合わせ数計算用の下準備
    # 1 ～ N の階乗・逆元・逆元の階乗を計算しておく
    n, k = map(int, input().split())
    MOD = 10**9 + 7
    fact = [1, 1]
    for i in range(2, n+1):
        fact.append((fact[-1] * i) % MOD)
    inv = [1, 1]
    for i in range(2, n+1):
        inv.append((-(MOD//i) * inv[MOD%i])%MOD)
    fact_inv = [1, 1]
    for i in range(2, n+1):
        fact_inv.append((fact_inv[-1]*inv[i])%MOD)

    # 0 人になりうる部屋の数
    max_zero = min(k, n-1)

    # 0 人になる部屋の数ごとに組み合わせ数を計算し、足し合わせていく
    result = 0
    for zr in range(max_zero+1):
        # 0 人になる部屋の組み合わせ数
        comb1 = (((fact[n] * fact_inv[n - zr]) % MOD) * fact_inv[zr]) % MOD

        # 他の部屋には最低一人いる。
        # 余りの zr 人を n - zr 箇所に重複ありで配置する組み合わせ数
        comb2 = (((fact[zr + (n-zr-1)] * fact_inv[zr]) % MOD) * fact_inv[n-zr-1]) % MOD

        # 組み合わせ数は、comb1 と comb2 を掛け合わせたものになる
        result = (result + comb1 * comb2) % MOD

    print(result)

main()
