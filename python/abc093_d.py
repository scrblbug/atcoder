# AtCoder Regular Contest 093 - D - Grid Components
# https://atcoder.jp/contests/arc093/tasks/arc093_b
# tag: グリッド 特殊構造

# ######
# ######
# ######
# ......
# ......
# ......
# ↑まずこんな感じで作成し、それぞれの間に
# .#.#.#.#.#
# ##########
# .#.#.#.#.#
# ##########
# こういう感じで別の色をはめ込んでいく。
# グリッドの制約条件は十分に広いので、余裕を持って
# 作成可能。

def main():
    A, B = map(int, input().split())

    field = [['#'] * 100 for _ in range(50)] + \
            [['.'] * 100 for _ in range(50)]

    # 適当にジェネレーターを作成し、そこから
    # 追加の座標を作成する
    def gen_white_pos():
        for r in range(0, 49, 2):
            for c in range(0, 50, 2):
                yield (r, c)
    
    def gen_black_pos():
        for r in range(99, 50, -2):
            for c in range(0, 50, 2):
                yield (r, c)
    
    gw = gen_white_pos()
    for w in range(A-1):
        r, c = next(gw)
        field[r][c] = '.'
    
    gb = gen_black_pos()
    for b in range(B-1):
        r, c = next(gb)
        field[r][c] = '#'
    
    # 回答出力。広さは100 100で決め打ち
    print(100, 100)
    for r in field:
        print(''.join(r))

main()
