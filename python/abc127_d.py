# AtCoder Beginner Contest 127 D - Integer Cards
# https://atcoder.jp/contests/abc127/tasks/abc127_d
# tag: 考察

# 最大効率でカードの交換を行った場合、結局のところ
# 最初に持っているカード + 書き換え後の数字が書かれたカード の集合から
# 上位 N 枚のカードを選んだのと同じ状態になる。

# というわけで、全てのカードを数字ごとに整理しなおし、
# 上位 N 枚の数字の合計を求めることにする。
def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    changes = [list(map(int, input().split())) for _ in range(M)]

    # カードの数字ごとに何枚あるかを保存
    cnt = dict()

    # 最初に持っているカードを数える
    for a in A:
        if a not in cnt:
            cnt[a] = 0
        cnt[a] += 1

    # 書き換え後のカードを数える
    for b, c in changes:
        if c not in cnt:
            cnt[c] = 0
        cnt[c] += b

    # 数字を大きい順にソート
    cards = list(cnt.keys())
    cards.sort(reverse=True)

    # N 枚になるまで大きい数字から順番に取る
    taken = 0
    result = 0
    for card in cards:
        n = cnt[card]
        if taken + n < N:
            result += card * n
            taken += n
        else:
            n = N - taken
            result += card * n
            break

    print(result)

main()
