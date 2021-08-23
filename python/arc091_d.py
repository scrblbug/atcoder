# AtCoder Regular Contest 091 D - Remainder Reminder
# https://atcoder.jp/contests/arc091/tasks/arc091_b
# tag: 整数 数え上げ 剰余

# a % b >= K (1 <= a <= N, 1 <= b <= N) が条件。
# a に対応する b を数えるのは大変そうなので、
# b を動かしながら、それぞれの a の個数を数えることにする。
# 以下、数えやすいように a を 0 ～ N の N+1 個の範囲で
# 動かすとする。

# b を固定して a を動かすと、a % bの値は
# (0, 1, 2, ..., b-1) の b 個の数をループすることになる。

# このループ中の、条件を満たす数は b - K 個。
# また、ループ自体は (N+1) // b 個がまるまる含まれる
# ことになるので、
# (b - K) * ((N+1) // b) 個の a が、まず存在する。
# ただし、K == 0 のケースのみ、0 が数えられてしまうので
# 1 引いておくこと。

# 加えて、(N + 1) % b 個のループの余りが存在する。
# ここに含まれる、条件を満たす数は
# max(0, (N + 1) % b - K) 個となる。

def main():
    N, K = map(int, input().split())

    result = 0

    # b は明らかに K より大きい
    for b in range(K+1, N+1):
        # まるごと含まれるループ分を加算
        num_in_loop = (b - K)
        loop_n = (N + 1) // b
        result += num_in_loop * loop_n

        # 便宜上 a を 0 からとして考えているので、
        # 含まれてしまう場合は 1 引いておく。
        if K == 0:
            result -= 1

        # ループの余り分を加算
        remainder = (N + 1) % b
        result += max(0, remainder - K)

    print(result)

main()
