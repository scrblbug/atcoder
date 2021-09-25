# AtCoder Beginner Contest 188 E - Peddler
# https://atcoder.jp/contests/abc188/tasks/abc188_e
# tag: グラフ DP 高橋国

# 問題の条件より、町はあらかじめトポロジカルソートされていると
# みなすことが出来る。
# よって、DPの要領で左側から順番に値を決定していけば良さそう。

# 決定していく値は、その町に到着するまでに通った町における、
# 一番安い金の価格とすればいい。

# これにより、それぞれの町において、過去一番安いところで
# 金を買った場合の金額を求められるので、それを元に
# それぞれの町で金を売った場合の利益を計算できる。
# その利益の最大値が答えとなる。

def main():
    N, M = map(int, input().split())
    prices = list(map(int, input().split()))
    path_dat = [list(map(int, input().split())) for _ in range(M)]

    paths = [[] for _ in range(N)]
    for a, b in path_dat:
        paths[a-1].append(b-1)

    # それぞれの町より手前の町での一番安い金の価格を
    # 配るDPで決定していく。
    result = -10**10
    min_buy_prices = [10**10] * N
    for now in range(N):
        # 次の町での金の最小価格は、今の町より前での金の最小価格と、
        # 今の町での金の価格のどちらか安い方。
        # （を、全ての経路において確認したものになる）
        pr = min(min_buy_prices[now], prices[now])
        for nxt in paths[now]:
            min_buy_prices[nxt] = min(min_buy_prices[nxt], pr)

        # 今いる街で金を売った場合の売買の利益を計算する。
        profit = prices[now] - min_buy_prices[now]
        if result < profit:
            result = profit

    print(result)

main()
