# AtCoder Beginner Contest 163 D - Sum of Large Numbers
# https://atcoder.jp/contests/abc163/tasks/abc163_d
# tag: 数え上げ MOD

# 1 ~ N を全て足したとしても、10^100 よりは小さくなる。
# つまり、この問題の本質は、足した数字の個数がカウント
# されるようになっているということ。
# また、10^100 部については、個数をカウントすることで
# これを無視していい。

# よって、まずいくつの数字を使うのかを考え、それぞれで
# どのような和を作ることが可能かを調べていくことになる。

# ところで、使う数字については連続した数字から自由に
# 選べるので、その和も連続した一定の範囲になる。
# つまり、和の最小値と最大値を調べれば、和の個数については
# (最大値 - 最小値) + 1 で簡単に得られる。


def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7

    result = 0
    # num 個の数字を使用するとする
    for num in range(K, N+2):
        # 和の最小は、0 ～ num-1 までの和
        min_sum = (0 + (num-1)) * num // 2
        # 和の最大は、(N-num+1) ～ N までの和 
        max_sum = ((N-num+1) + N) * num // 2

        result = (result + (max_sum - min_sum + 1)) % MOD

    print(result)

main()
