# 全国統一プログラミング王決定戦予選 D - Restore the Tree
# https://atcoder.jp/contests/nikkei2019-qual/tasks/nikkei2019_qual_d
# tag: グラフ 木 トポロジカルソート

# 書き加えられた有向辺を含む部分を考えると、
# 1 → 2 → 3 → 4
# 1     →     4
# となっているときに、4 の親を 1 ではなく 3 と
# 判定してやる問題といっていい。
# これは 1 2 3 4 がトポロジカルソートされているとして、
# 4 への辺がある頂点のうち一番最後のものを選べばいい、
# ということ。

def main():
    N, M = map(int, input().split())
    path_dat = [list(map(int, input().split())) for _ in range(N+M-1)]

    paths = [[] for _ in range(N+1)]

    # 各頂点への入辺数を管理
    edge_in = [0] * (N+1)

    # 隣接リストと共に、入辺数を数えておく
    for a, b in path_dat:
        paths[a].append(b)
        edge_in[b] += 1

    # トポロジカルソート
    # 入辺数が 0 のものをソート済みとしてリストに追加し、
    # そこから伸びる辺を削除するのを繰り返す
    t_sorted = []
    queue = [v for v in range(1, N+1) if edge_in[v]==0]
    while queue:
        now = queue.pop()
        t_sorted.append(now)

        for nxt in paths[now]:
            # 入辺を削除し、0 になったものだけをキューに追加
            edge_in[nxt] -= 1
            if edge_in[nxt] == 0:
                queue.append(nxt)

    # 親を管理するリスト
    parents = [0] * (N+1)

    # トポロジカルソート順に親を上書きしていけば、
    # 自動的に最後の入辺元を親にできる。
    for v in t_sorted:
        for v_to in paths[v]:
            parents[v_to] = v
    
    for p in parents[1:]:
        print(p)

main()

