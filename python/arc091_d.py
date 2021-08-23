# AtCoder Regular Contest 091 D - Remainder Reminder
# https://atcoder.jp/contests/arc091/tasks/arc091_b
<<<<<<< HEAD
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
=======
# tag: 整数 剰余 コーナーケース 高橋君

# a % b >= K

# N, K = 10, 2 で考えてみる。
# つまり、10 以下の整数 a, b で、a % b >= 2

# 必然的に、b > 2
# b = 3 の時
# a % 3 = 2 より、a = 2, 5, 8

# b = 4 の時
# a % 4 = 2 or 3 より、a = 2, 3, 6, 7, 10

# b = 5 の時
# a % 5 = 2 or 3 or 4 より、a = 2, 3, 4, 7, 8, 9

# ...

# のように、
# b によって決まる余りの数の種類は(b - K)個。
# これが何周か分あって、さらに N を超えない範囲でいくつか
# 存在する場合がある。

# b = 4 の場合を参考に、具体的に考えてみる。
# 10 までの数は、便宜的に 0 からカウントを始めると、
# まず (0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10)
# に分割できる。
# これらを mod b に変換してやると、
# (0, 1, 2, 3), (0, 1, 2, 3), (0, 1, 2)
# この中から、K 以上のものの数を数えればいい。
# みたいな。

# (0, 1, 2, 3) は各一種類ずつ余りが存在するので、まとめて
# 考慮可能。その数は b - K 個ずつが(N+1) // b グループある。

# 後は端の余っている分を考える。
# これは、(0, 1, ..., (N+1) % b - 1) なので
# (N+1) % b - K 個となる。
>>>>>>> 3ee3d223e157d907080f9a200b39f3ae9b653434

def main():
    N, K = map(int, input().split())

    result = 0

<<<<<<< HEAD
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

=======
    # b を K+1 ～ N の範囲に動かして考える。
    for b in range(K+1, N+1):
        # 上記考察でいうところの、(1, 2, 3, 4) のようなセット数。
        # 条件に合う余りは、b - K 種類。
        set_n = (N+1) // b
        result += set_n * (b - K)

        # (1, 2, ..., rem) のうち、条件に合う余りの数を求める。
        rem = (N+1) % b
        result += max(0, rem - K)

        # ただし、K = 0 の場合は a = 0 の場合を含んでしまうので
        # result から 1 を引いておく。
        if K == 0:
            result -= 1

>>>>>>> 3ee3d223e157d907080f9a200b39f3ae9b653434
    print(result)

main()
