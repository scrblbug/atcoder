# AtCoder Beginner Contest 220 F - Distance Sums 2
# https://atcoder.jp/contests/abc220/tasks/abc220_f
# tag: グラフ 木 距離 総和 DFS 全方位木DP 考察

# とりあえずある頂点を根として考え、回答を求めてみる。

# つぎに、その隣の頂点に注目したときに距離がどのように
# 変化するかを考えると……
# 1) その頂点を根とする部分木の要素数分距離が減る。
# 2) それ以外の要素数分、距離は増える。

# 以上の操作を繰り返す、つまり次々に隣の頂点へと
# 移ることで、全ての回答を求めることが出来る。

# 再帰制限を外しておく。
import sys
sys.setrecursionlimit(10**7)
def main():
    N = int(input())
    path_dat = [list(map(int, input().split())) for _ in range(N-1)]

    paths = [[] for _ in range(N)]
    for u, v in path_dat:
        u -= 1
        v -= 1
        paths[u].append(v)
        paths[v].append(u)

    # とりあえず 0 を根としてDFSを行い、
    # 各要素への距離の合計（回答）のついでに
    # 各頂点を根とする部分木の要素数も求めておく。
    result = [-1] * N # -1:未訪問 0:未確定
    partial = [0] * N

    def dfs(now):
        result[now] = 0
        ans = 0
        part = 0
        for nxt in paths[now]:
            if result[nxt] == 0:
                continue
            dfs(nxt)
            ans += result[nxt] + partial[nxt]
            part += partial[nxt]
        result[now] = ans
        partial[now] = part + 1
        return

    dfs(0)

    # 1回目のDFSが終わった段階で、
    # partialには各部分木の要素数が入っており、
    # result は result[0] のみ正しい値になっている。

    # 改めて、頂点を移動しながらそれぞれの正しい値を求めていく。
    queue = [[-1, 0]]
    while queue:
        prev, now = queue.pop()
        for nxt in paths[now]:
            if nxt == prev:
                continue
            result[nxt] = result[now] - partial[nxt] + (N - partial[nxt])
            queue.append([now, nxt])
    
    for r in result:
        print(r)

main()

