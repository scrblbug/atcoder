# AtCoder Beginner Contest 007 C - 幅優先探索
# https://atcoder.jp/contests/abc007/tasks/abc007_3
# tag: BFS 基礎問題 高橋君

# 普通に幅優先探索すればいい。
from collections import deque
def main():
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())

    # 0-indexed にする
    sy -= 1
    sx -= 1
    gy -= 1
    gx -= 1

    field = [[c for c in input()] for _ in range(R)]

    # 距離を保存する。 -1 なら未訪問。
    dist = [[-1] * C for _ in range(R)]

    # 動き方をあらかじめ持っておくと楽。
    moves = ((1, 0), (-1, 0), (0, -1), (0, 1))

    queue = deque([(sx, sy)])
    dist[sy][sx] = 0

    while queue:
        x_now, y_now = queue.popleft()
        for dx, dy in moves:
            x_nxt, y_nxt = x_now + dx, y_now + dy

            # 範囲チェック
            if not (0 <= x_nxt < C and 0 <= y_nxt < R):
                continue

            # 訪問済みかどうかと、壁チェック
            if dist[y_nxt][x_nxt] != -1 or field[y_nxt][x_nxt] == '#':
                continue

            dist[y_nxt][x_nxt] = dist[y_now][x_now] + 1
            queue.append((x_nxt, y_nxt))
    
    print(dist[gy][gx])

main()
