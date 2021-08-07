# AtCoder Regular Contest 004 B - 2点間距離の最大と最小 ( Maximum and Minimum )
# https://atcoder.jp/contests/arc004/tasks/arc004_2
# tag: 計算幾何 基礎問題

# 一番長い辺が、その他の辺の合計よりも長い場合は、
# 十分に折り返すことができず、長い分必ず余ってしまう。

# 逆にそれ以外の場合は、必ず点 N を点 0 の位置に
# 持ってくることができる。

def main():
    N = int(input())
    edges = [int(input()) for _ in range(N)]

    total = sum(edges)
    max_len = max(edges)

    # 一番長い辺が、その他の合計より長い場合
    if max_len > total - max_len:
        print(total)
        print(max_len * 2 - total)

    # そうでなければ、最短距離は 0 にできる
    else:
        print(total)
        print(0)

main()
