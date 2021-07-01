# AtCoder Beginner Contest 145 D - Knight
# https://atcoder.jp/contests/abc145/tasks/abc145_d
# tag: 二項係数 順列・組み合わせ 逆元 MOD 典型問題 コーナーケース


# まず何回動かすことになるのかを求める。（ n とする）
# 一手進むごとに、座標の x, y に (+2, +1) もしくは (+1, +2)
# される。つまり、必ず合計では +3 されることになる。
# つまり、全体での手数 n = (X + Y) // 3
# このとき、 X + Y が 3 で割り切れなければ到達不可能。
# また、毎手番かならず +1 はされるので、
# X < n or Y < n の場合も到達不可能。

# さて、この全体での手数のうち、x に +2 される回数を
# d 回とすると、n + d = X となることから、
# d = X - n
# あとは、n 回から d 回を選ぶ通り数、
# つまり n C d を求めることになる。

# また、最終的に MOD を用いた組み合わせ数計算になるので、
# 事前に逆元の階乗を計算しておくことにする。

def main():
    X, Y = map(int, input().split())
    MOD = 10**9 + 7

    # 到達不可能
    if (X + Y) % 3 != 0:
        print(0)
        return

    # 到達不可能その2
    n = (X + Y) // 3
    if X < n or Y < n:
        print(0)
        return

    d = X - n

    # このときの、nCd を求めたい。

    # 下準備
    # まず階乗のmodから
    fact = [1, 1]
    for i in range(2, n+1):
        fact.append((fact[-1] * i) % MOD)
    
    # 次に、逆元のmodを計算していく。
    # この際、次の計算を利用する。
    # aの逆元をA、q, rをp/aの商と余り、rの逆元をRとしたとき、
    # p = qa + r 両辺に A を掛けて
    # 0 = q + Ar (mod p) 両辺に R を掛けて
    # 0 = qR + A (mod p)
    # A = -qR (mod p)
    # 最初の仮定より r < a なので、下から順番に
    # 逆元を求めていくことができる。
    inv = [1, 1]
    for i in range(2, n+1):
        inv.append((-(MOD // i) * inv[MOD % i]) % MOD)

    # 次に、逆元の階乗のmodを求めていく
    inv_fact = [1, 1]
    for i in range(2, n+1):
        inv_fact.append((inv_fact[-1] * inv[i]) % MOD)
    
    # 改めて、
    # nCd = n! / (d! * (n-d)!) より
    result = (((fact[n] * inv_fact[d]) % MOD) * inv_fact[n-d]) % MOD

    print(result)

main()

