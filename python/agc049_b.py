# AtCoder Grand Contest 049 B - Flip Digits
# https://atcoder.jp/contests/agc049/tasks/agc049_b
# tag: 数列 隣接操作 考察

# ひとまず、数字2つの並びについて考察してみる。
# 00 → 操作不能
# 01 → 10
# 10 → 操作不能
# 11 → 00

# つまり、この操作は
# 1 を左に一つ移動させる
# 11 を 00 に書き換える
# といった感じの操作であることが分かる。

# 1 は左にしか移動させられないので、
# 逆に左端から一致させていく操作を考える。

# S と T それぞれの一番左端にある（未確認の） 1 のインデックスを、
# それぞれ i, j とする。

# このとき、

# i >= j なら、S[i] の 1 を j の位置まで移動させる。

# i < j なら、この 1 は消す必要があるので、S 上の次の 1 を
# 隣まで持ってきて、消してやる。

# という操作を繰り返してやることで、問題を解くことができる。

def main():
    N = int(input())
    S = [int(c) for c in input()]
    T = [int(c) for c in input()]

    # S と T の 1 の場所を確認しておく。
    # 1 が無くなったとき用に、最後に -1 を入れておく。
    s_ones = [i for i, v in enumerate(S) if v==1] + [-1]
    t_ones = [i for i, v in enumerate(T) if v==1] + [-1]

    # S, T それぞれのいくつめの 1 を見ているかを持っておく。
    s_idx = 0
    t_idx = 0

    result = 0
    while True:
        i = s_ones[s_idx]
        j = t_ones[t_idx]

        # 両方の 1 を確認し終えたら終了。
        if i == -1 and j == -1:
            break

        # S の 1 が尽きて、T にまだ 1 が残っている＝一致不可能。
        if i == -1 and j != -1:
            result = -1
            break

        # T に 1 が残っていて、S の 1 の場所の方が右にあるなら、
        # T と一致するまで移動させ、次の 1 を確認する。
        if j != -1 and i >= j:
            result += i - j
            s_idx += 1
            t_idx += 1

        # そうでないなら、S の次の 1 を持ってきて、
        # 11 として消去してやる。
        else:
            nxt = s_ones[s_idx+1]
            # 次の 1 が残ってない場合もある。
            if nxt == -1:
                result = -1
                break
            # 隣まで移動して、消す。
            else:
                result += nxt - i
                s_idx += 2

    print(result)

main()

