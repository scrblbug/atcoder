# AtCoder Regular Contest 123 C - 1, 2, 3 - Decomposition
# https://atcoder.jp/contests/arc123/tasks/arc123_c
# tag: 整数 分解 桁ごと

# K = 1, 2, 3 の時は、各桁に繰り上がりが起こらないので
# 比較的容易に判定可能。
# K >= 4 の時は繰り上がりが発生するので、難しくなる。

# 下の桁から順番に考えていくことにする。

# 一番下の桁を p としたとき、
# K <= 10*n + p <= 3 * K
# である必要がある。（ n は繰り上がり分）

# ここで、まず K = 5 の場合を考えてみる。
# すると、
# 5 <= 10*n + p <= 15
# となるが、これは上の桁に 1 繰り上げることを許せば
# 任意の数字を選ぶことが出来るということを意味する。

# また、繰り上げることが出来ないケースは、一番上の桁を
# 考慮している時に限られる。
# 一番上の桁については 5 回 "以下" であればいいので、
# やはり作成可能。

# つまり、K <= 5, n = 0 or 1 であるとしていい。

# 逆に言えば、K = 1, 2, 3, 4 と順に見ていき、
# 該当しなければ 5 としてもよい。

# 改めて、ある数字 N が K 回で作成可能かどうかの判定を行うとき、
# 一番下の桁を p とする。
# p もしくは 10 + p のどちらかを使用することになる。
# これを r とする。
# 一番下の桁を決定した後の数字について、
# (N - r) // 10 が K 回以下で作成可能であれば、
# 全体として K 回で作成可能、ということになる。

# ので、再帰で書くのが楽そう。

def main():
    T = int(input())
    queries = [int(input()) for _ in range(T)]
    # 数字 N が K 回以下で作成可能かどうか
    def check(N, K):
        if N == 0:
            return True

        p = N % 10

        # 現在以下の K について上の桁を確認する
        for k in range(K, 0, -1):
            # 繰り上がりのない場合
            if k <= p <= 3*k:
                nxt = N // 10
                if check(nxt, k) == True:
                    return True

            # 繰り上がりのある場合
            if k <= 10 + p <= 3 * k:
                nxt = N // 10 - 1
                if nxt >= 0 and check(nxt, k):
                    return True

        # K 回以下で上の桁を構築できない ＝ False
        return False

    for N in queries:
        for i in range(1, 5):
            if check(N, i):
                print(i)
                break
        else:
            print(5)

main()
