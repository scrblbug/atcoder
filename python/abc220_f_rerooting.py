# 全方位木DPを利用した解法は以下の通り。
# 再帰を用いずに書いてあるので、Pypyでもそこそこの速度になる。

# 扱う値は
# [頂点～各要素への距離の合計, 頂点を含む部分木の要素数]
# 併合時は単純に合計し、調整時に要素数を加えて距離の合計を更新する。

def main():
    N = int(input())
    path_dat = [list(map(int, input().split())) for _ in range(N-1)]

    paths = [[] for _ in range(N)]
    for u, v in path_dat:
        u -= 1
        v -= 1
        paths[u].append(v)
        paths[v].append(u)

    # 併合・仕上げ調整関数の定義。
    def merge(v1, v2):
        return [v1[0] + v2[0], v1[1] + v2[1]]
    def finish(val):
        return [val[0] + val[1], val[1] + 1]

    # 単位元の定義。
    ie = [0, 0]

    # 初回DFS
    result = [None] * N
    done = [0] * N # 0:未訪問 1:行きに通った 2:完了
    partial = [[] for _ in range(N)]
    idx_list = [[] for _ in range(N)]
    queue = [0]
    while queue:
        now = queue.pop()
        # 行きがけ
        if done[now] == 0:
            done[now] = 1
            queue.append(now)
            for nxt in paths[now]:
                if done[nxt] == 0:
                    queue.append(nxt)
        # 帰りがけ
        else:
            ans, num = 0, 0
            done[now] = 2
            result[now] = ie
            for nxt in paths[now]:
                if done[nxt] == 1:
                    continue
                partial[now].append(result[nxt])
                idx_list[now].append(nxt)
                result[now] = merge(result[now], result[nxt])
            result[now] = finish(result[now])

    # ここからrerooting。
    par_res = [None] * N
    queue = [0]
    done = [0] * N
    while queue:
        now = queue.pop()
        done[now] = 1
        csum_l = [ie]
        csum_r = [ie]

        if par_res[now] != None:
            partial[now].append(par_res[now])

        # 左右累積和を作成。
        for r in partial[now]:
            csum_l.append(merge(csum_l[-1], r))
        for r in partial[now][::-1]:
            csum_r.append(merge(csum_r[-1], r))

        # 最終値を確定させる。
        result[now] = finish(csum_l[-1])

        # 累積和を使用した、子への伝播。
        for i in range(len(idx_list[now])):
            nxt = idx_list[now][i]
            if done[nxt] == 1:
                continue
            left = csum_l[i]
            right = csum_r[len(partial[now])-1-i]
            prop = finish(merge(left, right))
            par_res[nxt] = prop
            queue.append(nxt)

    for r in result:
        print(r[0])

main()
