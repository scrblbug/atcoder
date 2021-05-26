# AtCoder Beginner Contest 202 E - Count Descendants
# https://atcoder.jp/contests/abc202/tasks/abc202_e
# tag: 木 部分木 深さ オイラーツアー 二分探索

# クエリの意味するところは、根を 1 とする木において
# ノード U 以下の部分木にある 深さ D のノードの個数、
# ということ。

# そこで、まずは深さ別にまとめてやることを考える。
# また、部分木が絡むことから、オイラーツアーを利用する。
# すなわち、各深さにおいてオイラーツアーの in をまとめておき、
# 祖先 U の in ～ out 間にある、対象の深さにある in の数を
# 答えていく……という流れ。

from bisect import bisect_left
def main():
    N = int(input())
    path_dat = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]

    # 隣接リストに変換
    paths = [[] for _ in range(N+1)]
    for i, parent in enumerate(path_dat, start=2):
        paths[parent].append(i)
    
    # オイラーツアーを行いノード別の in / out と 深さを取得
    et_in = [-1] * (N+1)
    et_out = [-1] * (N+1)
    et_depth = [-1] * (N+1)
    order = 0
    depth = 0
    queue = [~1, 1]
    while queue:
        now = queue.pop()
        if now >= 0:
            et_in[now] = order
            et_depth[now] = depth
            depth += 1
            for nxt in paths[now]:
                queue.append(~nxt)
                queue.append(nxt)
        else:
            et_out[~now] = order
            depth -= 1
        order += 1

    # 深さ別の in をまとめ、ソートしておく
    max_depth = max(et_depth)
    in_by_depth = [[] for _ in range(max_depth+1)]

    for i in range(1, N+1):
        in_by_depth[et_depth[i]].append(et_in[i])
    
    for l in in_by_depth:
        l.sort()

    # クエリ処理開始
    for u, d in queries:
        # 深さ D のノードがそもそも無ければ 0 を返す
        if d > max_depth:
            print(0)
            continue

        a_in = et_in[u]
        a_out = et_out[u]

        # 左端と右端をそれぞれ二分探索する
        left = bisect_left(in_by_depth[d], a_in)
        right = bisect_left(in_by_depth[d], a_out)
        print(right - left)

main()
