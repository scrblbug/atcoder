# AtCoder Beginner Contest 040 C - 柱柱柱柱柱
# https://atcoder.jp/contests/abc040/tasks/abc040_c
# tag: DP 典型問題 基礎問題

# 典型的かつ基礎的なDPで解ける問題。
# dp_table[i] = i+1 番目の柱に行くための最小コスト
# として、スタート地点から順に更新していく
# i+1 番目としているのは、0-indexed でテーブルを作成するからで、
# それ以上の意味はない。（1 番目の柱に行くコスト = dp_table[0] = 0）

# この DP が成立するのは、各移動を独立して考えることが可能なため。
# つまり、どのような経路を通って移動したかが問われないので、
# i 番目の柱にコスト c で到達できた場合、その結果のみで
# 計算結果をまとめることが出来る。

# 逆に今回の DP が使えないケースを考えてみると、
# 例えば2回連続で2個先の柱に飛ぶ時は（疲れるので）コストが x 増える
# みたいな場合には、前回の行動を組み込む必要があるため、
# まとめ方が変わる ＝ 違ったDPを使う必要がある。
# 具体的には、さらに場合を分けて
# dp_table[i][prev] = i+1 番目の柱に前回 prev+1 歩進んだ時のコスト
# みたいな感じで行うことになる……はず？

def main():
    N = int(input())
    pillars = list(map(int, input().split()))

    # dp用テーブル（名前を dp とする人が多いけど、個人的には dpt）
    dpt = [10**10] * N

    # 最初の柱はコスト 0 なので、設定しておく
    dpt[0] = 0

    # いわゆる配るDPで、わかりやすいように
    # やや回りくどく書いていくと……
    for now in range(N-1):
        # 次の柱に飛ぶ場合
        next_p = now + 1

        # トータルのコストを計算し、最小値に更新する
        cost = dpt[now] + abs(pillars[next_p] - pillars[now])
        dpt[next_p] = min(dpt[next_p], cost)

        # 二個先の柱に飛ぶ場合
        next_next_p = now + 2

        # 行き過ぎる時は計算しない
        if next_next_p >= N:
            continue

        # トータルのコストを計算し、最小値に更新する
        cost = dpt[now] + abs(pillars[next_next_p] - pillars[now])
        dpt[next_next_p] = min(dpt[next_next_p], cost)
    
    print(dpt[-1])

main()


# ついでに、もらうDPでも……
def main2():
    N = int(input())
    pillars = list(map(int, input().split()))

    dpt = [10**10] * N
    dpt[0] = 0

    for now in range(1, N):
        prev_p = now - 1
        cost = dpt[prev_p] + abs(pillars[now] - pillars[prev_p])
        dpt[now] = min(dpt[now], cost)

        prev_prev_p = now - 2
        if prev_prev_p < 0:
            continue
        cost = dpt[prev_prev_p] + abs(pillars[now] - pillars[prev_prev_p])
        dpt[now] = min(dpt[now], cost)
    
    print(dpt[-1])

# main2()


# せっかくなのでメモ化再帰でも
# 再帰の深さ制限を解除しておかないとREになるので注意
import sys
sys.setrecursionlimit(10**9)
def main3():
    N = int(input())
    pillars = list(map(int, input().split()))

    memo = [-1] * N
    memo[0] = 0

    def get_min_cost(pos):
        if memo[pos] != -1:
            return memo[pos]

        cost = get_min_cost(pos - 1) + abs(pillars[pos-1] - pillars[pos])

        if pos > 1:
            cost = min(cost, get_min_cost(pos-2) + abs(pillars[pos-2] - pillars[pos]))

        memo[pos] = cost

        return cost
    
    print(get_min_cost(N-1))

# main3()
