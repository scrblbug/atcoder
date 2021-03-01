# Code Formula 2014 main F - 100個の円
# https://atcoder.jp/contests/code-formula-2014-final/tasks/code_formula_2014_final_f
# tag: グリッド 詰め込み

# あまり何も考えずに、グリッドに対する正方形の詰め込みとして
# 頑張ってみる。広さからするとたぶんいける……？

# 問題の本質としては、円の詰め込みを正方形の詰め込みに
# 切り替えること、ということだと思われる。

def main():
    # 一応は多少効率を考えて、縦200をワンセットとする。
    # (100, 0) (99, 1).... の正方形の組を縦に二つずつ入れていく
    # みたいな感じで……
    # 50がダブっちゃうけど上書きなのであまり気にしない。通れば正義。
    result = [[] for _ in range(101)]
    offset_y = 0
    offset_x = 0
    for r in range(100, 49, -1):
        if offset_x + 2 * r> 1500:
            offset_x = 0
            offset_y += 200
        result[r] = [offset_x + r, offset_y + r]
        result[100-r] = [offset_x + (100-r), offset_y + 2*r + (100-r)]
        offset_x += 2 * r

    for x, y in result[1:]:
        print(x, y)

    # 以下念のため、問題文に沿った全探索によるチェック
    # for i, c1 in enumerate(result):
    #     for j, c2 in enumerate(result[i+1:],start=i+1):
    #         x1, y1 = c1
    #         x2, y2 = c2
    #         if (x2-x1)**2 + (y2-y1)**2 < (i+j)**2:
    #             print(x1, y1, i, x2, y2, j)

    # 通ったので、これで。
main()
