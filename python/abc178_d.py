# AtCoder Beginner Contest 178 D - Redistribution
# https://atcoder.jp/contests/abc178/tasks/abc178_d
# tag: 数列 総和 数え上げ DP

# S = x の時の答えを、f(x) と書くとする。
# f(x) が成立する数列が存在するとして、そのそれぞれの数列の
# 最後の要素を除いたものを考えると……
# f(x) = f(x-3) + f(x-4) + ... + f(0) となる

# 例：f(10) を求めたい時、その答えは
# {(何か合計 7 になる数列), 3} の通り数 = f(7)
# {(何か合計 6 になる数列), 4} の通り数 = f(6)
# .....
# の合計、すなわち
# f(7) + f(6) + ... + f(0)

# というわけで、あまり何も考えずに下から決定していく DP を書いてみる。
def main2():
    S = int(input())
    MOD = 10**9 + 7

    dpt = [0] * (S + 1)

    # 合計を 1, 2 にできる数列は存在しないが、
    # 0 にできる数列は空数列の 1 通りあるとみなせる
    dpt[0] = 1

    for now in range(3, S + 1):
        for prev in range(now - 2):
            dpt[now] = (dpt[now] + dpt[prev]) % MOD
    
    print(dpt[S])

# main2()

# 上記の書き方だと、O(N^2) 。
# 今回の問題なら十分間に合うが、実は
# f(x) = f(0) + f(1) + ... + f(x-4) + f(x-3)
# = (f(0) + ... + f(x-4)) + f(x-3)
# = f(x-1) + f(x-3)
# に気づくと、O(N) になる。

def main():
    S = int(input())
    MOD = 10**9 + 7

    dpt = [0] * (S + 1)
    dpt[0] = 1

    for now in range(3, S + 1):
        dpt[now] = (dpt[now - 1] + dpt[now - 3]) % MOD
    print(dpt[S])

main()

# 実は行列演算＆二乗繰り返し法だとか、FFTだとかに近い発想で
# もっと計算量を落とせる……らしいが、数学力が 0 なので分からない。
# この段階でそこまで考える必要も無いだろう。うん。