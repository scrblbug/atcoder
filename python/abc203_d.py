# AtCoder Beginner Contest 203 D - Pond
# https://atcoder.jp/contests/abc203/tasks/abc203_d
# tag: グリッド 中央値 二分探索 二次元累積和 AtCoder公園 高橋君

def main():
    N, K = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]

    # 求める最小の中央値がある値以下かどうかを判定
    def check_median(med):
        above = [[n > med for n in field[y]] for y in range(N)]
        
        # 二次元累積和を取っておく
        csum = [[0] * (N+1) for _ in range(N+1)]
    
        for y in range(1, N+1):
            tmp = 0
            for x in range(1, N+1):
                tmp += above[y-1][x-1]
                csum[y][x] = tmp + csum[y-1][x]

        # 範囲の左上を(sx, sy)として全探索
        for sy in range(N-K+1):
            for sx in range(N-K+1):
                # 二次元累積和を利用して、med より大きな数を数える
                count = csum[sy+K][sx+K] - csum[sy+K][sx] - csum[sy][sx+K] + csum[sy][sx]

                # med より大きな数が、半分以下なら中央値は med 以下
                if count <= (K*K) // 2:
                    return True
        else:
            return False

    # 二分探索
    left = -1
    right = 10**9

    while right - left > 1:
        mid = (left + right) // 2
        if check_median(mid):
            right = mid
        else:
            left = mid
    
    print(right)

main()
