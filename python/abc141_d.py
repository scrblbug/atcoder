# AtCoder Beginner Contest 141 D - Powerful Discount Tickets
# https://atcoder.jp/contests/abc141/tasks/abc141_d
# tag: 優先度付きキュー 典型問題

# 優先度付きキューを知っていれば簡単に解けるが、
# 知らなければ解くのが困難になる、典型問題。

# 要するに、割引券を使うごとに品物が半額になる。
# 割引券の枚数が一定であることを考えると、
# ある割引券をどの品物に使用するかを考えたとき、
# もっとも高い品物に対して使用したい。

# 値段でソートする → 一番高い品物に割引券を使う → 
# 値段でソートする → 一番高い……とループさせるわけだが、
# そのままだと計算量が O(MN) となってしまうので、
# 制約 (1 <= N, M <= 10^5) からすると間に合わない。
# が、ここで優先度付きキューを使用すると、O(M logN) で
# 解くことができるので、間に合う。みたいな。

import heapq
def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 優先度付きキューは小さい順に出てくるため、
    # あらかじめ値を負にしておく
    items = [-v for v in A]
    heapq.heapify(items)

    # そのまま //2 すると、負の値で切り捨てがずれるので注意。
    # そのため、一旦正の値に戻している。
    # ここで切り捨ててもいい根拠については、
    # 一般に正の整数 x, a, b について
    # (x // a) // b == x // (a * b) となるためだが、
    # 厳密な証明は省略。ごく単純に考えるなら、整数演算ではなく
    # 有理数演算として捉えた場合、余りは全て小数部として表す
    # ことができるが、それは当然 0 <= r < 1 の範囲に留まるため……
    # みたいな雑な理解でもいいかもしれない。
    for _ in range(M):
        max_price = -heapq.heappop(items)
        heapq.heappush(items, -(max_price//2))
    
    result = -sum(items)
    print(result)

main()
