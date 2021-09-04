# AtCoder Grand Contest 033 A - Darker and Darker
# https://atcoder.jp/contests/agc033/tasks/agc033_a
# グリッド キュー BFS

# 毎回グリッドを全て探索していては、間に合わない。
# ところで、毎回の操作で黒マスが少しずつ増えていくわけだが、
# その操作で黒マスになるのは、前回の操作で黒マスになった
# 地点の隣だけである。

# つまり、毎回全マスを探索するのではなく、前回黒マスになった
# 隣のマスだけを探索すればいい。これは一種のBFSとなる。
# 均すと、全てのマスは一回ずつ探索されることになるので
# O(HW) となる。

from collections import deque
def main():
    H, W = map(int, input().split())
    field = [[c for c in input()] for _ in range(H)]

    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

    # 黒マスに変わった手数を保存しておく配列。
    # まだ白マスなら -1。
    done = [[-1] * W for _ in range(H)]

    # 初回のキューの作成
    queue = deque()
    for y in range(H):
        for x in range(W):
            if field[y][x] == '#':
                queue.append((x, y))
                done[y][x] = 0

    result = 0

    # 探索開始
    while queue:
        x, y = queue.pop()
        for dx, dy in moves:
            tx, ty = x + dx, y + dy

            # 黒マスの隣がまだ白なら、黒マスに変えてキューの左に追加。
            if 0 <= tx < W and 0 <= ty < H and done[ty][tx] == -1:
                done[ty][tx] = done[y][x] + 1
                queue.appendleft((tx, ty))
                if result < done[ty][tx]:
                    result = done[ty][tx]

    print(result)

main()
