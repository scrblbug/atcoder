# ある色のボールを取り除ける条件は、上にあるボールが
# 取り除かれていることである。

# そこで、各色を頂点として、各色からひとつ下にある
# 色に対して辺を張るようなグラフを構築する。

# 入辺が存在しない頂点と、そこから出ている辺を順に
# 取り除いていき、全ての頂点を取り除けるならば
# 答えは 'Yes' になる。

# ちなみに、これはトポロジカルソートと同じ操作になっている。

def main():
    N, M = map(int, input().split())
    tubes = []
    for _ in range(M):
        k = int(input())
        tubes.append(list(map(int, input().split())))

    removed = []

    # 頂点ごとの入辺の数。
    edge_in = [0] * (N+1)

    # グラフを構築する。
    paths = [[] for _ in range(N+1)]
    for balls in tubes:
        for i in range(len(balls)-1):
            paths[balls[i]].append(balls[i+1])
            edge_in[balls[i+1]] += 1

    # 入辺の無いものを抽出。
    no_edge_in = [idx for idx, n in enumerate(edge_in) if n == 0]

    # 入辺が無いものと、そこからの辺をどんどん取り除いていく。
    while no_edge_in:
        color = no_edge_in.pop()
        removed.append(color)
        for nxt in paths[color]:
            edge_in[nxt] -= 1
            if edge_in[nxt] == 0:
                no_edge_in.append(nxt)
    
    # 1-indexed にしている関係で、取り除かれる頂点は N+1 個。
    if len(removed) == N + 1:
        print('Yes')
    else:
        print('No')

main()
