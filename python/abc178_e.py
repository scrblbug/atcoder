# AtCoder Beginner Contest 178 E - Dist Max
# https://atcoder.jp/contests/abc178/tasks/abc178_e
# tag: グリッド マンハッタン距離 最大距離 基礎問題

# 点 (x1, y1), (x2, y2) の距離は、x1 と x2, y1 と y2 の
# 大小関係から、次の 4 通りのうち最大のものになる。

# 1. (x1 - x2) + (y1 - y2)
# 2. (x2 - x1) + (y1 - y2)
# 3. (x1 - x2) + (y2 - y1)
# 4. (x2 - x1) + (y2 - y1)

# ところで、各 (x, y) の
# x + y = A, x - y = S とおいて上記の式を置き換えてみると、

# 1. (x1 + y1) - (x2 + y2) = A1 - A2
# 2. -(x1 - y1) + (x2 - y2) = S2 - S1
# 3. (x1 - y1) - (x2 - y2) = S1 - S2
# 4. -(x1 + y1) + (x2 + y2) = A2 - A1

# となるので、結局は A の差分 or S の差分、ということになる。

# つまり、各点ごとの x + y, x - y の値から距離を計算できる。
# これをあらかじめ計算し、それぞれの最大値から最小値を
# 引くことで、その差分の最大値を容易に計算可能。

# この値は、各点の座標軸に対して45度傾いた直線上への写像と捉える
# こともできる。これは、実際にグリッド上に x+y, x-y の値を
# 書き込んでいけば、すぐに分かると思う。

def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]

    # x+y, x-y をリストに。
    rot1 = [x+y for x, y in points]
    rot2 = [x-y for x, y in points]

    # 最大値から最小値を引いたものを比較する。
    print(max(max(rot1)-min(rot1), max(rot2)-min(rot2)))

main()
