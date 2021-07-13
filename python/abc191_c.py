# AtCoder Beginner Contest 191 C - Digital Graffiti
# https://atcoder.jp/contests/abc191/tasks/abc191_c
# グリッド 画像 数え上げ

# 角が現れるパターンは、以下の通り。

# 内角90度の角。順に右下、左下、右上、左上が角
#  #.  .#  ..  ..
#  ..  ..  #.  .#

# 内角270度の角で、同様。
#  ##  ##  #.  .#
#  #.  .#  ##  ##

# これらのパターンが、角がある場合には必ず現れ、
# かつ、同じ角は二つ以上の条件にあてはまらない。

# よって、4マスずつスキャンしていき、上記の
# パターンが現れれば角の数に +1すればいい。

# 上記のパターンは 4マス中 1マス or 3マスが
# 黒、という条件で簡単に判別できる。

def main():
    H, W = map(int, input().split())
    # 黒マスを 1、白マスを 0 に変換しておく
    field = [[1 if c == '#' else 0 for c in input()] for _ in range(H)]

    # 4マスずつ見ていき、黒マスが 1 or 3 マスなら答えに +1。
    result = 0
    for y in range(H-1):
        for x in range(W-1):
            cnt = field[y][x] + field[y+1][x] + field[y][x+1] + field[y+1][x+1]
            if cnt == 1 or cnt == 3:
                result += 1

    print(result)

main()
