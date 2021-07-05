# AtCoder Beginner Contest 039 D - 画像処理高橋君
# https://atcoder.jp/contests/abc039/tasks/abc039_d
# tag: グリッド 変換 隣接処理 高橋君

# 条件より、変換後の画像においてあるマスが白だった場合、
# 変換前の画像ではそのマス及び隣接マスが白である必要がある。

# これによって変換前の画像を推測した後、実際にうまくいくか
# どうかを確認する。

def main():
    H, W = map(int, input().split())
    after = [[c for c in input()] for _ in range(H)]

    nb = ((-1, -1), (0, -1), (1, -1),
          (-1, 0), (0, 0), (1, 0),
          (-1, 1), (0, 1), (1, 1))

    # 黒で初期化し、白マスを定めていく
    before = [['#'] * W for _ in range(H)]

    for y in range(H):
        for x in range(W):
            # 変換後が白なら、変換前の同じ場所と隣接を白に
            if after[y][x] == '.':
                for dx, dy in nb:
                    tx, ty = x + dx, y + dy
                    if not (0 <= tx < W and 0 <= ty < H):
                        continue
                    before[ty][tx] = '.'
    
    # 実際に操作を行ってみる
    test = [['.'] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if before[y][x] == '#':
                for dx, dy in nb:
                    tx, ty = x + dx, y + dy
                    if not (0 <= tx < W and 0 <= ty <H):
                        continue
                    test[ty][tx] = '#'
    
    # 一致すれば出力。一致しなければ、不可能。
    if after == test:
        print('possible')
        for r in before:
            print(''.join(r))
    else:
        print('impossible')

main()

