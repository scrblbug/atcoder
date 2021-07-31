# AtCoder Beginner Contest 129 D - Lamp
# https://atcoder.jp/contests/abc129/tasks/abc129_d
# tag: グリッド スキャン すぬけ君

# 光源の置き方毎に愚直に行うと、O(HW(H+W))となり、
# やや間に合わない。
# 縦方向の広がりと横方向の広がりは独立していると考えられるので、
# とりあえず横方向だけを考慮してみる。

# #..#....##. のような状態の時、横方向への広がりの大きさは
# 02204444001 といった感じになるので、これを求める。

# 同様に縦方向の広がりも求め、合計すればいい。

def main():
    H, W = map(int, input().split())
    field = [input() for _ in range(H)]

    horizontal = [[0] * W for _ in range(H)]
    vertical = [[0] * W for _ in range(H)]

    # 往復スキャンしつつ、横方向の広がりを求める。
    # 以下のコードの場合、壁は -1 となるが、
    # どこかに空きマスがあることは保証されているので
    # 気にしないことにする。
    for y in range(H):
        tmp = 0
        for x in range(W):
            if field[y][x] == '#':
                tmp = 0
            else:
                tmp += 1
            horizontal[y][x] += tmp

        tmp = 0
        for x in range(W-1, -1, -1):
            if field[y][x] == '#':
                tmp = 0
            else:
                tmp += 1
            horizontal[y][x] += tmp - 1

    # 同様に、縦方向の広がりを求める。
    for x in range(W):
        tmp = 0
        for y in range(H):
            if field[y][x] == '#':
                tmp = 0
            else:
                tmp += 1
            vertical[y][x] += tmp
        
        tmp = 0
        for y in range(H-1, -1, -1):
            if field[y][x] == '#':
                tmp = 0
            else:
                tmp += 1
            vertical[y][x] += tmp - 1

    result = 0

    # 光源の置き方を全探索する
    for y in range(H):
        for x in range(W):
            # 実際には光源のマスを重複して数えているので、1 引く
            tmp_r = horizontal[y][x] + vertical[y][x] - 1

            if result < tmp_r:
                result = tmp_r

    print(result)

main()
