# Xi < Yi の条件により、閉路は存在せず、全ての経路は
# どこかで終端になる。
# そこで、ここではメモ化再帰を用いて解いてみる。
# すなわち、get_max_price(x): x から到達可能な町での、
# 最も高い金の価格を返す。
# 終了条件は、経路の終端。ここでは売れる地点がないので、
# 仮に -inf を返すことにする。

import sys
sys.setrecursionlimit(10**9)
def main():
    N, M = map(int, input().split())
    prices = list(map(int, input().split()))
    path_dat = [list(map(int, input().split())) for _ in range(M)]

    paths = [[] for _ in range(N)]
    for a, b in path_dat:
        paths[a-1].append(b-1)

    memo = [None] * N

    # 再帰関数による定義。
    def get_max_price(x):
        if memo[x] != None:
            return memo[x]
        result = -10**10

        for nxt in paths[x]:
            result = max(result, prices[nxt], get_max_price(nxt))

        memo[x] = result
        return result

    # 改めて、全地点を調べて最大利益を求める。
    result = -10**10
    for i in range(N):
        buy = prices[i]
        sell = get_max_price(i)
        if result < sell - buy:
            result = sell - buy

    print(result)

main()
