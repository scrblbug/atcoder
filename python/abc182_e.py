# AtCoder Beginner Contest 182 E - Akari
# https://atcoder.jp/contests/abc182/tasks/abc182_e
# tag: グリッド スキャン 数え上げ

# 上下左右の方向をそれぞれ独立したものとして考えると、楽。
# 仮に ライト: o , ブロック: # とすると、
# ライトが現れた後を明るく、ブロックが現れた後を暗くするだけでいい。
# 具体的な例として、
# ...o...#..
# のような並びがあり、明かりが届く範囲を 1 にしたいとする。
# 左→右 の方向だけに注目すると、
# 0001111000
# 右→左 だと
# 1111000000
# これを合成すると、
# 1111111000
# という具合にできる。縦方向も同様。

def main():
    H, W, N, M = map(int, input().split())
    lights = [list(map(int, input().split())) for _ in range(N)]
    blocks = [list(map(int, input().split())) for _ in range(M)]

    # 0: 空白, 1: ライト, -1: ブロック
    field = [[0] * W for _ in range(H)]
    for ly, lx in lights:
        field[ly-1][lx-1] = 1
    for by, bx in blocks:
        field[by-1][bx-1] = -1

    result = [[0] * W for _ in range(H)]

    for y in range(H):
        # 左 → 右
        lit = 0
        for x in range(W):
            if field[y][x] == -1:
                lit = 0
                continue
            if field[y][x] == 1:
                lit = 1
            if lit == 1:
                result[y][x] = 1
        # 右 → 左
        lit = 0
        for x in range(W-1, -1, -1):
            if field[y][x] == -1:
                lit = 0
                continue
            if field[y][x] == 1:
                lit = 1
            if lit == 1:
                result[y][x] = 1

    for x in range(W):
        # 上 → 下
        lit = 0
        for y in range(H):
            if field[y][x] == -1:
                lit = 0
                continue
            if field[y][x] == 1:
                lit = 1
            if lit == 1:
                result[y][x] = 1
        # 下 → 上
        lit = 0
        for y in range(H-1, -1, -1):
            if field[y][x] == -1:
                lit = 0
                continue
            if field[y][x] == 1:
                lit = 1
            if lit == 1:
                result[y][x] = 1

    # 数えて回答
    print(sum(result[y][x]==1 for y in range(H) for x in range(W)))

main()
