# AtCoder Beginner Contest 140 D - Face Produces Unhappiness
# https://atcoder.jp/contests/abc140/tasks/abc140_d
# tag: 考察 列 反転

# 不幸になっている人は、端を除けば必ず 'RL' の形を取っている。

# (1人以上のR) (1人以上のL) が列内に存在していると仮定した場合、
# このどちらかの集団をまるごと反転してやることで、
# 不幸な人を 2人減らすことが可能。
# つまり、一回の操作につき不幸な人を 2人ずつ減らせることになる。

# ただし、
# [端] (1人以上のR) (1人以上のL) [端]
# というケースのみ、不幸な人数は 2人 → 1人 にしかならない。
# これは、最低でも一人不幸な人がいる、という最低値の条件と
# 見なすことができる。

def main():
    N, K = map(int, input().split())
    S = input()

    # 初期状態の不幸な人数を数える
    unhappy = S.count('RL') * 2
    if S[0] == 'L':
        unhappy += 1
    if S[-1] == 'R':
        unhappy += 1

    # 不幸な人数は、操作回数 * 2 減らせる。ただし 0 にはできない。
    unhappy = max(1, unhappy - 2*K)

    print(N - unhappy)

main()
