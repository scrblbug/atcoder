# AtCoder Regular Contest 037 B - バウムテスト
# https://atcoder.jp/contests/arc037/tasks/arc037_b
# tag: グラフ 木 閉路 BFS DFS 高橋君 典型問題

# 閉路検出の典型問題。
# BFS、もしくは DFS で各連結成分の探索を行い、
# 途中で訪問済みの頂点が現れた場合は
# 閉路が存在する ＝ 木では無い。
# 逆に閉路が存在しなければ、木となる。

def main():
    N, M = map(int, input().split())
    path_dat = [list(map(int, input().split())) for _ in range(M)]

    paths = [[] for _ in range(N)]

    for u, v in path_dat:
        paths[u-1].append(v-1)
        paths[v-1].append(u-1)

    result = 0

    visited = [False] * N

    # 各頂点をスタートとして、連結成分を全てチェックしていく
    for start in range(N):
        # 訪問済みならスキップ
        if visited[start]:
            continue

        # 木かどうかのチェック用
        is_tree = True

        visited[start] = True
        queue = [(-1, start)]
        while queue:
            prev, now = queue.pop()
            for nxt in paths[now]:
                # 一つ前に戻る経路はスキップする。
                if nxt == prev:
                    continue
                # 訪問済みの頂点が現れたら、木では無い。
                if visited[nxt]:
                    is_tree = False
                    continue
                visited[nxt] = True
                queue.append((now, nxt))

        # 木なら回答に +1
        result += is_tree

    print(result)

main()
