# AtCoder Beginner Contest 138 D - Ki
# https://atcoder.jp/contests/abc138/tasks/abc138_d
# tag: グラフ 木 部分木 BFS DFS

# BFS もしくは DFS にて探索を行えば、根 → 葉 と進むことになるので、
# 細かいことは気にせず、順次子へと加算値を伝播させて行けばいい。

def main():
    N, Q = map(int, input().split())
    path_dat = [list(map(int, input().split())) for _ in range(N-1)]
    add_dat = [list(map(int, input().split())) for _ in range(Q)]

    # 0-indexedへ
    paths = [[] for _ in range(N)]
    for a, b in path_dat:
        a -= 1
        b -= 1
        paths[a].append(b)
        paths[b].append(a)
    
    # 加算値 兼 回答
    counter = [0] * N
    for n, x in add_dat:
        counter[n-1] += x

    # BFS による探索    
    queue = [0]
    visited = [False] * N
    while queue:
        now = queue.pop()
        visited[now] = True

        for nxt in paths[now]:
            if visited[nxt]:
                continue
            # 親 → 子 と加算値を伝播させる
            counter[nxt] += counter[now]
            queue.append(nxt)

    print(*counter)

main()
