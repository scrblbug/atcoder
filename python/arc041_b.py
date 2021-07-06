# AtCoder Regular Contest 041 B - アメーバ
# https://atcoder.jp/contests/arc041/tasks/arc041_b
# tag: グリッド 考察

# 一番上の行から、順に決定できる。
# 分裂後の状態で一番上の行にアメーバがいるなら、
# 分裂前はひとつ下の行に同じ数のアメーバがいたことになる。
# すると、そのアメーバが上以外に分裂した個数も決定可能。
# 以下繰り返しで、順次決定していく。

def main():
    N, M =map(int, input().split())

    after = [[int(c) for c in input()] for _ in range(N)]
    before = [[0] * M for _ in range(N)]

    # 行ごとに見ていく
    for y in range(N-1):
        for x in range(M):
            # 分裂後にアメーバがいるなら、
            if after[y][x] > 0:
                # 分裂前の一行下にアメーバが同じ数いる
                before[y+1][x] = after[y][x]

                # そのアメーバが分裂してできたアメーバを
                # あらかじめ差し引いておく
                after[y+1][x-1] -= after[y][x]
                after[y+1][x+1] -= after[y][x]
                after[y+2][x] -= after[y][x]
    
    for r in before:
        print(''.join(map(str, r)))

main()
