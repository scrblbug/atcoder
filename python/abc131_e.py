# AtCoder Beginner Contest 131 E - Friendships
# https://atcoder.jp/contests/abc131/tasks/abc131_e
# tag: グラフ 特殊構造 距離

# 全体が連結となっている＝少なくとも N-1 本は辺を持つ。
# また、辺の両端にある頂点間の最短距離は 1 となる。
# つまり、すべての頂点の組み合わせ N*(N-1)//2 から N-1 を
# 引いたものが、最短距離 2 となる頂点の組み合わせの
# 最大数となる

def main():
    N, K = map(int, input().split())

    if K > (N * (N - 1)) // 2 - (N - 1):
        print(-1)
        return
    
    # 最短距離 2 となる頂点を最大数にするためには、
    # ある適当な一頂点（仮に 1 とする）から他の全ての頂点への
    # 辺のみが存在する構造であれば良い

    result = []

    for i in range(2, N+1):
        result.append((1, i))

    # また、この構造で 2～N の各頂点間の最短距離は全て 2 と
    # なるため、2～N の任意の2点間を結ぶ辺を追加することで、
    # 最短距離 2 となる組み合わせを一つ減らすことができる。
    
    # 適当な辺を順に出力するジェネレータ
    def generate_additional_edge():
        for a in range(2, N):
            for b in range(a+1, N+1):
                yield (a, b)

    tmp = generate_additional_edge()

    for i in range((N*(N-1))//2 - (N-1) - K):
        result.append(next(tmp))
    
    print(len(result))
    for a, b in result:
        print(a, b)

main()
