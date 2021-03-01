# AtCoder Beginner Contest 005 D - おいしいたこ焼きの焼き方
# https://atcoder.jp/contests/abc005/tasks/abc005_4
# tag: グリッド 累積和 因数分解

# 店員が焼けるたこ焼きの数の「上限」となっているので、
# 結局のところ「一度に焼くたこ焼きの数」（1～N^2）ごとに、
# そのおいしさの最大値を求めてやる必要がある。

# そこで(左上, 右下)の組で全探索を行うことにすることで、
# 全パターンを網羅するようにする。

def main():
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]

    Q = int(input())
    shopkeepers = [int(input()) for _ in range(Q)]

    # とりあえず二次元累積和を作成
    # 後のために0からスタートさせる(1-indexed)
    csum_field = [[0] * (N+1)]
    for row in field:
        csum_row = [0]
        tmp = 0
        for c, n in enumerate(row, start=1):
            tmp += n
            csum_row.append(tmp + csum_field[-1][c])
        csum_field.append(csum_row)

    # 累積和を利用して合計値を求める関数を持っておく
    def get_sum(sx, sy, ex, ey):
        return csum_field[ey+1][ex+1] - csum_field[ey+1][sx] - csum_field[sy][ex+1] + csum_field[sy][sx]

    # たこ焼きを焼く数ごとに美味しさの最大値を求めていく
    max_taste = [0] * (N*N + 1)
    for sy in range(N):
        for sx in range(N):
            for ex in range(sx, N):
                for ey in range(sy, N):
                    n_tako = (ex-sx+1) * (ey-sy+1)
                    taste = get_sum(sx, sy, ex, ey)
                    if max_taste[n_tako] < taste:
                        max_taste[n_tako] = taste
    
    # 上限個数を決めたときの最大の美味しさを求め直す
    # ＝それまでに現れた数字の最大値となる
    result = []
    tmp = 0
    for t in max_taste:
        if tmp < t:
            tmp = t
        result.append(tmp)
    
    # 回答を出力
    for s in shopkeepers:
        print(result[s])

main()
