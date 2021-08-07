# AtCoder Regular Contest 023 B - 謎の人物X
# https://atcoder.jp/contests/arc023/tasks/arc023_2
# tag: グリッド 考察 高橋君

# 行き過ぎる場合でも、隣のマスと行ったり来たりして歩数を
# 稼ぐことが出来る。

# つまり、あるマスに最終的に止まることが出来る条件は、以下の通り。
# 1) 当該マスまでの最短距離が、歩く歩数以内かどうか
# 2) 当該マスまでの距離と歩数の偶奇が一致しているかどうか

def main():
    R, C, D = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(R)]

    result = 0

    # 各マスをチェックし、条件を満たすなら
    # そこのたこ焼きを食べることが可能。
    for r in range(R):
        for c in range(C):
            dist = r + c
            if dist <= D and dist % 2 == D % 2:
                if result < field[r][c]:
                    result = field[r][c]

    print(result)

main()
