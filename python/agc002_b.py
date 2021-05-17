# AtCoder Grand Contest 002 B - Box and Ball
# https://atcoder.jp/contests/agc002/tasks/agc002_b
# tag: 高橋君 考察

# 赤い玉が入っている箱 A から他の箱 B へ玉を移すと、
# 赤い玉は箱 A / B のどちらかに入っている可能性がある。

# ただし、ある箱の中身が空になる操作が行われると、
# その時点でその箱に赤い玉が入っている可能性は無くなる。

# 箱に赤い玉が含まれている可能性があるかどうかと、
# 箱の中の玉の数を管理しながら順次処理していく。

def main():
    N, M = map(int, input().split())
    ops = [list(map(int, input().split())) for _ in range(M)]

    # 赤い玉が含まれている可能性があるかどうか
    possible_red = [False] * (N+1)
    possible_red[1] = True

    # ボールの数
    ball_n = [1] * (N+1)

    for x, y in ops:
        # 赤い玉が含まれている可能性がある箱から移動
        if possible_red[x]:
            possible_red[y] = True
        
        # 玉の数を変更
        ball_n[x] -= 1
        ball_n[y] += 1

        # 玉が 0 個ならば、赤い玉も無い
        if ball_n[x] == 0:
            possible_red[x] = False

    # True は 1、False は 0 として計算される
    print(sum(possible_red))

main()
