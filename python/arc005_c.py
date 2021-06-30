# AtCoder Regular Contest 005 C - 器物損壊！高橋君
# https://atcoder.jp/contests/arc005/tasks/arc005_3
# tag: グリッド 探索 ダイクストラ

# 全探索っぽく距離を計算していくが、壁を壊す必要がある場合は、
# 探索をなるべく後回しにする。
# 探索の優先度については、キューの左右どちらに入れるかで
# 振り分ける。
from collections import deque
def main():
    H, W = map(int, input().split())
    field = [input() for _ in range(H)]

    for y in range(H):
        for x in range(W):
            if field[y][x] == 's':
                sx, sy = x, y
            if field[y][x] == 'g':
                gx, gy = x, y

    dist = [[-1] * W for _ in range(H)]
    dist[sy][sx] = 0

    moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
    queue = deque([(sx, sy)])
    while queue:
        x, y = queue.pop()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if nx < 0 or W <= nx:
                continue
            if ny < 0 or H <= ny:
                continue
            if dist[ny][nx] != -1:
                continue

            # 壁の時は後回しにする
            if field[ny][nx] == '#':
                dist[ny][nx] = dist[y][x] + 1
                queue.appendleft((nx, ny))

            # 壁じゃなければ先に探索
            else:
                dist[ny][nx] = dist[y][x]
                queue.append((nx, ny))

    if dist[gy][gx] <= 2:
        print('YES')
    else:
        print('NO')

main()


# 別のやり方として、 s から g までをダイクストラっぽく
# 探索していく手もある。その場合、'#' を通る場合のみ距離が増え、
# それ以外は距離が増えないことになる。
# 上のやり方に比べると、logN 分遅い感じ。

from heapq import heappush, heappop
def main2():
    H, W = map(int, input().split())
    field = [input() for _ in range(H)]

    for y in range(H):
        for x in range(W):
            if field[y][x] == 's':
                sx, sy = x, y
            if field[y][x] == 'g':
                gx, gy = x, y

    dist = [[10**18] * W for _ in range(H)]
    dist[sy][sx] = 0

    moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
    hq = [(0, sx, sy)]
    while hq:
        dist_now, x, y = heappop(hq)
        if dist[y][x] > dist_now:
            continue
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if nx < 0 or W <= nx:
                continue
            if ny < 0 or H <= ny:
                continue
            if field[ny][nx] == '#':
                nd = dist_now + 1
            else:
                nd = dist_now
            if dist[ny][nx] > nd:
                dist[ny][nx] = nd
                heappush(hq, (nd, nx, ny))

    if dist[gy][gx] <= 2:
        print('YES')
    else:
        print('NO')

# main2()
