# AtCoder Beginner Contest 195 F - Coprime Present
# https://atcoder.jp/contests/abc195/tasks/abc195_f
# tag: 素数 互いに素

# B - A <= 72 というのがポイント。
# 全ての整数の組み合わせは差分が 72 以下なので、
# 共通する因数も 72 以下となる。

# また、合成数を考慮する意味は特にないので
# 素因数のみを考えていく。

def main():
    A, B = map(int, input().split())

    # とりあえず 72 までの素数を出しておく。
    # 念の為、ここではエラトステネスの篩を用いている。
    primep = [True] * 73
    primep[0], primep[1] = False, False
    for i in range(2, 73):
        if primep[i] == True:
            for j in range(2*i, 73, i):
                primep[j] = False
    primes = [n for n in range(73) if primep[n]==True]

    # 各素因数をビットで管理するので、対応するインデックスを作っておく
    p_to_i = dict()
    for i, p in enumerate(primes):
        p_to_i[p] = i

    # dpt: {今使用している素因数のビット管理値: 通り数}
    # 初期値は {素因数なし: 1 通り}
    dpt = {0: 1}

    # 実際のところ、72 以下の素数は 20 個程度なので、
    # DPで十分間に合う

    for n in range(A, B+1):
        # DP更新用
        nxt_dpt = dict()

        # これから追加を検討する数字の素因数を確認、管理ビットを作成する
        pf_bit = 0
        for p in primes:
            if n % p == 0:
                pf_bit += 1<<(p_to_i[p])

        for st, cnt in dpt.items():
            # 使用しない場合を追加
            if st not in nxt_dpt:
                nxt_dpt[st] = 0
            nxt_dpt[st] += cnt
            
            # 使用できるなら使用したものを追加
            # ビット演算で素因数がかぶっていないかどうかを確認
            if st & pf_bit:
                continue

            # かぶっていなければ、新たな素因数集合に通り数を加える
            nxt_st = st | pf_bit
            if nxt_st not in nxt_dpt:
                nxt_dpt[nxt_st] = 0
            nxt_dpt[nxt_st] += cnt

        dpt = nxt_dpt

    # 最後は、全ての合計が求める答えとなる
    print(sum(dpt.values()))

main()
