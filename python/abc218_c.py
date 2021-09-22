# AtCoder Beginner Contest 218 C - Shapes
# https://atcoder.jp/contests/abc218/tasks/abc218_c
# tag: グリッド 一致判定 回転 平行移動

# 回転・平行移動を行ったときに、グリッド上の図形が
# 一致するかどうかを判定する問題。

# まず、グリッドの回転について。
# Python では zip() を利用すると回転操作を行いやすい。

# 左90度回転なら
# [row[::-1] for row in zip(*S)]

# 右90度回転なら
# [row for row in zip(*S[::-1])]

# 次に、平行移動を伴う一致判定について。

# 色々とやり方はあると思うが、ここでは '#' の存在する
# 座標を全列挙してリストにし、そのリストが一致しているか
# どうかで判定することにする。

# ただし、中に含まれる x座標の最小値と y座標の最小値を
# 求めておき、全ての座標からそれぞれの最小値を引いたもので
# 判定を行う。
# イメージとしては、左上に図形を押し付けてから一致するか
# どうかを判定することになる。

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]

    # まずは一致判定用に、'#' の座標リストを返す関数を
    # 作成しておく。左上に押し付ける処理も入れておく。
    def get_shape_id(shape):
        pos_list = []
        min_x = N
        min_y = N
        for y in range(N):
            for x in range(N):
                if shape[y][x] == '#':
                    if min_x > x:
                        min_x = x
                    if min_y > y:
                        min_y = y
                    pos_list.append([x, y])
        
        # x, y座標の最小値を引いてからリストを返す。
        return [[x-min_x, y-min_y] for x, y in pos_list]

    # 愚直に回転しながら比較する。
    if get_shape_id(S) == get_shape_id(T):
        print('Yes')
        return

    S = [row[::-1] for row in zip(*S)]
    if get_shape_id(S) == get_shape_id(T):
        print('Yes')
        return

    S = [row[::-1] for row in zip(*S)]
    if get_shape_id(S) == get_shape_id(T):
        print('Yes')
        return

    S = [row[::-1] for row in zip(*S)]
    if get_shape_id(S) == get_shape_id(T):
        print('Yes')
        return

    print('No')

main()
