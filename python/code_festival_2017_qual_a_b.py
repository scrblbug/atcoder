# CODE FESTIVAL 2017 qual A B- fLIP
# https://atcoder.jp/contests/code-festival-2017-quala/tasks/code_festival_2017_quala_b
# tag: グリッド 範囲操作 考察

# 各行・列のボタンに関しては、自由に入れ替え可能。
# よって、最終的に問題になるのは、それぞれいくつずつ
# 反転されているかということ。

# p 行分と q 列分のが反転している時、黒になっているマスの数を考えると、
# (M-q) * p + (N-p) * q となる。（図を書くと分かりやすい）

# というわけで、書く場合については O(1) で求めることができ、
# 制限が 1 <= N <= 1000, 1 <= M <= 1000 なので、全探索を行う。

def main():
    N, M, K = map(int, input().split())

    # 上記の式を用いて全探索
    for p in range(N+1):
        for q in range(M+1):
            # 見つかれば 'Yes' にして break
            if (M-q) * p + (N-p) * q == K:
                result = 'Yes'
                break
        else:
            continue
        # 多重ループ脱出用 break
        break
    # 見つからなければ 'No'
    else:
        result= 'No'

    print(result)

main()

# ところで、公式解説によると O(N) の解法があるとのこと。
# そこで、反転している行数 n を固定して考えてみる。
# すると、これから反転する m (0 <= m <= M) を動かした時に、
# 全体の黒の数は初期値を M * n として、 m を 1 増やす毎に
# N - n * 2 だけ増えていく。
# ということは、(K - M * n) を (N - n * 2) で割ったときの
# 商と余りを q, r とすると、 r = 0 かつ 0 <= q <= M の時に
# 条件を満たすことが分かる。

def main2():
    N, M, K = map(int, input().split())
    for n in range(N+1):
        # N == n * 2 のときは、m を動かしても黒の数が変化しない。
        # この場合は、初期値が K になっているかどうかで確認する。
        if N == n * 2:
            if K == M * n:
                print('Yes')
                break
        else:
            q, r = divmod(K - M * n, N - n * 2)
            if r == 0 and 0 <= q <= M:
                print('Yes')
                break
    else:
        print('No')

# main2()
