# AtCoder Beginner Contest 217 E - Sorting Queries
# https://atcoder.jp/contests/abc217/tasks/abc217_e
# tag: 優先度付きキュー deque 考察

# 操作により時、全体の列は常に
# [ソートされた数列] [ソート後に入力された順の数列]
# といった感じになる。

# つまり、優先度付きキューと deque を組み合わせることで、
# 操作を再現できる。

from collections import deque
from heapq import heappush, heappop
def main():
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]

    # 左側のソート済み列は、heapq を用いる。
    left = []

    # 右側のソート前分は、deque で保持する。
    right = deque()

    for q in queries:
        # 1 x の形式のクエリの時。
        # right に append(x) する。
        if len(q) == 2:
            op, x = q
            right.append(x)

        # 2 のクエリの時。
        elif q[0] == 2:
            # ソート済みの数列 (left) が残っている時は、
            # left から heappop する。
            if len(left) > 0:
                print(heappop(left))

            # そうでないときは、right から popleft する。
            else:
                print(right.popleft())
        
        # 3 のクエリの時。
        else:
            # いま残っている right の要素を、
            # 全て left に入れてやる。
            while right:
                heappush(left, right.pop())

main()
