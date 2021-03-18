# AtCoder Beginner Contest 035 B - ドローン
# https://atcoder.jp/contests/abc035/tasks/abc035_b
# tag: グリッド マンハッタン距離

# ひとまず不明な命令以外を見て、距離を測定する。
# 不明な命令の分を考える場合、マンハッタン距離のみに注目すると、
# どんな命令であっても距離は +1 もしくは -1 されることになる。
# あとは最大値と最小値を求めるだけだが、最小値を求める際は
# 最後に 0 → 1 → 0... と繰り返すことになるので、端に注意すること。

def main():
    S = input()
    T = int(input())

    # ドローンの座標、及び不明分の個数を持っておく
    pos_x, pos_y = 0, 0
    unknown = 0

    # 文字列の調査とともに、座標と不明分の更新
    for c in S:
        if c == 'L':
            pos_x -= 1
        elif c == 'R':
            pos_x += 1
        elif c == 'U':
            pos_y -= 1
        elif c == 'D':
            pos_y += 1
        else:
            unknown += 1

    # 不明分を除いたマンハッタン距離
    dist = abs(pos_x) + abs(pos_y)

    # 最大値の時は、足すだけでよい
    if T == 1:
        result = dist + unknown

    # 最小値の時は、行き過ぎることがあるので、
    # 超過分を 2 で割った余りを出す必要がある。
    # Python の % 演算は 0 以上を返してくれるのでこれでOK。
    else:
        result = dist - unknown
        if result < 0:
            result %= 2

    print(result)

main()

