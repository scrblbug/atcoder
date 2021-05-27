# AtCoder Regular Contest 120 C - Swaps 2
# https://atcoder.jp/contests/arc120/tasks/arc120_c
# tag: 数列 隣接入替 考察 転倒数 フェニック木

# 数字が左右に動く時、同時に +1 / -1 されることになる。
# とりあえずどの数字をどこに移動させるべきかを知りたいので、
# 一旦すべての数字を「左端ではなにになるか？」で統一してやる
# ことにすることで、見通しをよくする。

# f.e. （入力例 4 に基づく）
# A: 8 5 4 7 4 5    →   8 6 6 10 8 10
# B: 10 5 6 7 4 1   →   10 6 8 10 8 6

# まず、数字の数・種類が一致していれば変換可能ということになる。

# 問題はどの場所の数字をどこに動かすかだが、これは
# 実は左側（あるいは右側）から貪欲に合わせてやればいい。
# つまり、上記例なら A における n 番目の 8 を
# B における n 番目の 8 の場所に移動すればいい。

# 上記に基づき、A が B の何番目に移動するのかを
# まとめてやると、(0-indexed)
# a_to_b: 2 1 5 0 4 3
# となる。この転倒数が、求める答えとなる。

# 制約が 2 <= N <= 2*10^5 なので、
# 転倒数を求める際は BIT などをもちいて O(N logN) の計算量で
# おこなうこと。

from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # とりあえず扱いやすいように変換する
    A = [a+i for i, a in enumerate(A)]
    B = [b+i for i, b in enumerate(B)]

    # 変換後の数字の種類・数が一致しているか確認
    a_cnt = Counter(A)
    b_cnt = Counter(B)

    # 一致して無ければ -1 を返して終了
    if a_cnt != b_cnt:
        print(-1)
        return
    
    # B に置ける j 番目の i のインデックスを出しやすくしておく
    # f.e. B の2番目の8(0-indexed)の場所 → b_dic[8][1] = 2
    b_dic = dict()
    for i, b in enumerate(B):
        if b not in b_dic:
            b_dic[b] = []
        b_dic[b].append(i)
    
    # 移動先リスト
    a_to_b = []

    # 今までにどの数字がいくつ出てきているかを確認するための辞書
    a_dic = dict()

    # A を順番に見ていき、移動先リストを作成
    for a in A:
        if a not in a_dic:
            # 0-indexed のため
            a_dic[a] = -1
        a_dic[a] += 1

        # a_dic[a] : A で a が登場するのは何回目か
        a_to_b.append(b_dic[a][a_dic[a]])

    # 改めて、転倒数を求める
    # BIT （フェニック木）
    bit_sum = [0] * (N+1)
    def bit_add(idx, x):
        # 内部は 1-indexed
        idx += 1
        while idx < N+1:
            bit_sum[idx] += x
            idx += idx & -idx
    def bit_get_sum(idx):
        idx += 1
        result = 0
        while idx:
            result += bit_sum[idx]
            idx -= idx & -idx
        return result

    result = 0

    # 転倒数の計算
    # a_to_b には 0 ～ N-1 が一つずつ含まれている
    for i, n in enumerate(a_to_b):
        # 今までに現れた n より大きい数の個数
        # ＝ 全ての個数 - n 以下の個数
        result += i - bit_get_sum(n)
        
        # n の数に 1 を足す
        bit_add(n, 1)
    
    print(result)

main()
