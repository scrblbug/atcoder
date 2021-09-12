# AtCoder Regular Contest 032 B - 道路工事
# https://atcoder.jp/contests/arc032/tasks/arc032_2
# tag: グラフ 連結成分 BFS DFS 大工のチョーさん

# 連結成分数が分かれば、その数 - 1 の道路を
# 作れば、全てを連結にできる。

def main():
    N, M = map(int, input().split())
    path_dat = [list(map(int, input().split())) for _ in range(M)]

    # 隣接リストを作成
    paths = [[] for _ in range(N)]
    for a, b in path_dat:
        a -= 1
        b -= 1
        paths[a].append(b)
        paths[b].append(a)

    # あらかじめ 1引いておく。
    result = -1

    # 連結成分数を数える。
    visited = [False] * N
    for start in range(N):
        if visited[start] == True:
            continue

        result += 1
        queue = [start]

        while queue:
            now = queue.pop()
            for nxt in paths[now]:
                if visited[nxt] == True:
                    continue
                visited[nxt] = True
                queue.append(nxt)

    print(result)

main()
