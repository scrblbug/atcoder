# AtCoder Beginner Contest 109 D - Make Them Even
# https://atcoder.jp/contests/abc109/tasks/abc109_d
# tag: グリッド 隣接操作

# 条件を逆にいうと、全マス一回ずつ操作が可能。

# そこで、一番上の行から、各行ごとに順にマスを見ていき、
# コインが奇数枚なら一行下へ 1枚移動させていく。

# 最後の行は、左端から順に見ていき、奇数枚なら
# ひとつ右へと移動させることにする。

# これで、少なくとも一番右下のマス以外を、全て偶数に
# することができる。

def main():
    H, W = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(H)]

    result = []

    # 各行ごとに見ていく。
    for y in range(H-1):
        for x in range(W):
            # 奇数なら、ひとつ下へ 1枚移動。
            if field[y][x] % 2 != 0:
                field[y][x] -= 1
                field[y+1][x] += 1
                result.append([y+1, x+1, y+2, x+1])

    # 最後の行。
    for x in range(W-1):
        # 奇数なら、ひとつ右へ 1枚移動。
        if field[H-1][x] % 2 != 0:
            field[H-1][x] -= 1
            field[H-1][x+1] += 1
            result.append([H, x+1, H, x+2])

    print(len(result))
    for r in result:
        print(*r)

main()
