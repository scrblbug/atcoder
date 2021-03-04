# AtCoder Beginner Contest 148 F - Playing Tag on Tree
# https://atcoder.jp/contests/abc148/tasks/abc148_f
# tag: 木 ゲーム 距離

# 高橋君が青木君に捕まらない範囲で青木くんから一番遠くに逃げ、
# そこでつかまるイメージ
# ただし、必ず移動しなければならないため、葉で捕まることはなく、
# かならず葉のひとつ手前で捕まる or 捕まりに行くことになる

# 高橋君が移動可能な範囲とは、結局の所、高橋君の方が
# 青木くんよりも近い地点、ということになる

def main():
    N, u, v = map(int, input().split())
    path_dat = [list(map(int, input().split())) for _ in range(N-1)]
    paths = [[] for _ in range(N+1)]
    for a, b in path_dat:
        paths[a].append(b)
        paths[b].append(a)

    taka_dist = [-1] * (N+1)
    aoki_dist = [-1] * (N+1)

    # 距離のリストを（dist上に）作成する探索
    def make_dist_list(start, dist):
        dist[start] = 0
        queue = [(-1, start)]
        while queue:
            prev, now = queue.pop()
            for nxt in paths[now]:
                if nxt == prev:
                    continue
                dist[nxt] = dist[now] + 1
                queue.append((now, nxt))
    
    # 各ノードの高橋君・青木君からの距離を算出
    make_dist_list(u, taka_dist)
    make_dist_list(v, aoki_dist)

    # 高橋君の移動可能な範囲で、青木君から一番遠いところを見つける
    result = 0
    for td, ad in zip(taka_dist[1:], aoki_dist[1:]):
        if td < ad and result < ad:
            result = ad

    # 実際に捕まるところは、一歩手前
    print(result - 1)

main()
