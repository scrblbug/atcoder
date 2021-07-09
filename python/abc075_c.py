# AtCoder Beginner Contest 075 C - Bridge
# https://atcoder.jp/contests/abc075/tasks/abc075_c
# tag: グラフ 連結 BFS DFS 橋 愚直

# 愚直に辺を一つずつ外し、連結になっているかどうか
# 確かめていく。

# 制約が緩いので、分かりやすさ優先で……
def main():
    N, M = map(int, input().split())
    path_dat = [list(map(int, input().split())) for _ in range(M)]

    result = 0

    for i in range(M):
        # 対象の辺を外してグラフを構築、連結かどうか確認する
        in_use = path_dat[:i] + path_dat[i+1:]

        paths = [[] for _ in range(N)]
        for a, b in in_use:
            paths[a-1].append(b-1)
            paths[b-1].append(a-1)

        # ここから探索
        visited = [False] * N
        visited[0] = True
        # 訪れた頂点数を記録していく
        cnt = 1
        queue = [0]
        while queue:
            now = queue.pop()
            for nxt in paths[now]:
                if visited[nxt]:
                    continue
                visited[nxt] = True
                queue.append(nxt)
                cnt += 1
        
        # 訪れた頂点数 != N なら、連結ではない
        if cnt != N:
            result += 1
    
    print(result)

main()
