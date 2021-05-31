# AtCoder Beginner Contest 151 D - Maze Master
# https://atcoder.jp/contests/abc151/tasks/abc151_d
# tag: グリッド 再長距離 BFS 高橋君 青木君

# どこからスタートするのかについて、全探索する。
# 一回一回の各最長距離については、BFS で取得すればいい。

from collections import deque
def main():
    H, W = map(int, input().split())
    field = [input() for _ in range(H)]

    # BFS で距離を算出し、最大のものを返す関数を作っておく
    def get_longest(sx, sy):
        moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
        dist = [[-1] * W for _ in range(H)]
        dist[sy][sx] = 0
        queue = deque([(sx, sy)])
        while queue:
            now_x, now_y = queue.popleft()
            for dx, dy in moves:
                nxt_x, nxt_y = now_x + dx, now_y + dy
                if not(0 <= nxt_x < W and 0 <= nxt_y < H):
                    continue
                if dist[nxt_y][nxt_x] == -1 and field[nxt_y][nxt_x] == '.':
                    dist[nxt_y][nxt_x] = dist[now_y][now_x] + 1
                    queue.append((nxt_x, nxt_y))
        return max(v for row in dist for v in row)

    result = 0
    # スタート地点を全て試す
    for x in range(W):
        for y in range(H):
            if field[y][x] == '#':
                continue
            tmp_r = get_longest(x, y)
            if tmp_r > result:
                result = tmp_r

    print(result)

main()
