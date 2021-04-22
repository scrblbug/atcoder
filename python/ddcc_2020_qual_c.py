# DISCO presents ディスカバリーチャンネルコードコンテスト2020予選 C - Strawberry Cakes
# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_c
# tag: グリッド 分割

# 何通りも解き方はあると思うけど……ここではとりあえず

# イチゴがある行の場合：
# イチゴの右横で分割し、最後のイチゴは右端まで含めて取る
# f.e. ..#.#..#.. → 1112233333

# イチゴが無い行の場合：
# 上下の行にある分割に合わせる。これは適当でいい。

# 以上の方針で、
# .......    1222233
# #...#.#    1222233
# ..#...#    4445555
# .......    4445555
# .#..#..    6677777
# .......    6677777

# といった感じの分割になり、いけそう＆比較的楽に実装できそう。

def main():
    H, W, K = map(int, input().split())
    field = [input() for _ in range(H)]

    result = [[] for _ in range(H)]

    # 行をチェックしながら、イチゴのある行を分割していく
    no_sb = []
    # 現在の区分け
    piece = 1
    for y, raw in enumerate(field):
        # イチゴがなければ、行数だけ保存してスキップ
        if '#' not in raw:
            no_sb.append(y)
            continue
        # イチゴがあるなら、とりあえず場所をチェック
        sb_pos = []
        for x, c in enumerate(raw):
            if c == '#':
                sb_pos.append(x)
        # イチゴの場所を元に分割を作成
        now = 0
        for pos in sb_pos[:-1]:
            for i in range(now, pos+1):
                result[y].append(piece)
            piece += 1
            now = pos + 1
        # 最後の一個は行の終わりまで取る
        for i in range(now, W):
            result[y].append(piece)
        piece += 1
    
    # 次に、イチゴが無かった行を決定していく。
    # 適当に、上からと下から二回合わせていってやればいい。
    for y in no_sb:
        if y != 0:
            result[y] = result[y-1]
    for y in no_sb[::-1]:
        if y != H - 1:
            result[y] = result[y+1]
    
    for r in result:
        print(*r)

main()

