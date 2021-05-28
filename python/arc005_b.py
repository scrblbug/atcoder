# AtCoder Regular Contest 005 B - P-CASカードと高橋君
# https://atcoder.jp/contests/arc005/tasks/arc005_2
# tag: グリッド 反射 高橋君

# 反射するのをどう扱うか考える問題。
# 解き方はいろいろあると思われる。
def main():
    x, y, w = input().split()
    x = int(x) - 1
    y = int(y) - 1

    field = [[c for c in input()] for _ in range(9)]

    dx, dy = 0, 0
    if 'U' in w:
        dy -= 1
    if 'D' in w:
        dy += 1
    if 'L' in w:
        dx -= 1
    if 'R' in w:
        dx += 1
    
    result = []

    # ここでは、0123456787654321をワンセットと考え、
    # まず %= 16 したあと、前半部ならそのまま、
    # 後半部なら折り返す……みたいな発想で求めている。
    # このやり方は（今回は必要ないが）、何度も反射を
    # 繰り返す場合でも対応可能。
    for i in range(4):
        now_x = x % 16 if x % 16 < 9 else 16 - x % 16
        now_y = y % 16 if y % 16 < 9 else 16 - y % 16
        result.append(field[now_y][now_x])
        x += dx
        y += dy
    
    print(''.join(result))

main()
