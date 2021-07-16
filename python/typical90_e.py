# 桁DPの遷移を考える。
# dpt[n][r] : n 桁の数字で mod B が r となる通り数。

# 一桁ずつ増やす基本の遷移はこれ。
# 全ての r, usable に対して、
# dpt[n+1][(r*10 + {usable}) % B] += dpt[n][r]

# ちなみにこの遷移は行列演算に帰結できるので、行列累乗が使える。
# ……のでやってみたが、間に合わなかった。厳しい。

# ところで、ここに d 桁一気に追加できないだろうか？
# dpt[n+d][(r * 10**d + ??) % B] の通り数を考えることになる。

# この ?? の全パターンを考えるわけだが、これは実は
# dpt[d][s] の全ての s を考えるのに等しい。
# となると、全ての r, s に対して
# dpt[n+d][((r * 10**d) + s) % B] += dpt[n][r] * dpt[d][s]

# これは何を意味しているかというと、
# 'ABCDE' の 5 桁の数があるとして、これを 'ABC' と 'DE' に
# 分割することが出来る。
# このとき、'ABCDE' が mod B において t になる組み合わせ数は、
# 'ABC' が r になり、'DE' が s になるとするとき (mod B)、
# r * 10**d + s = t となるような全ての組み合わせの合計となる。

# 以上のように、dpt[x] と dpt[y] （と、10**y % B）が
# 求まっていれば dpt[x+y] を求めることが出来るので、
# どうにかなりそう。

def main():
    N, B, K = map(int, input().split())
    nums = list(map(int, input().split()))
    MOD = 10**9 + 7

    # ダブリングによって答えを求める予定なので、
    # それに応じた添字としておく。

    # N を2進数にしておく
    n_bin = bin(N)[2:][::-1]

    # p10_rem[i]: 10**(2**i) % B
    p10_rem = [10 % B]
    for i in range(len(n_bin)-1):
        p10_rem.append((p10_rem[-1] ** 2) % B)

    # dpt[i][j]: 2**i 桁の数字における、mod B が
    # j になるような数字の通り数
    dpt = [[0] * B for _ in range(len(n_bin))]

    # 1桁の場合を作成
    for n in nums:
        dpt[0][n % B] += 1

    # 2**i 桁の数字の通り数を作成していく
    for i in range(len(n_bin)-1):
        for r in range(B):
            for s in range(B):
                nxt = (r * p10_rem[i] + s) % B
                dpt[i+1][nxt] = (dpt[i+1][nxt] + dpt[i][r] * dpt[i][s]) % MOD

    # ダブリングにより、回答を求める
    result = []
    for i, b in enumerate(n_bin):
        if b == '1':
            if result == []:
                result = dpt[i]
                continue

            new_r = [0] * B
            for r in range(B):
                for s in range(B):
                    nxt = (r * p10_rem[i] + s) % B
                    new_r[nxt] = (new_r[nxt] + result[r] * dpt[i][s]) % MOD
            result = new_r

    print(result[0])

main()


