# AtCoder Beginner Contest 095 D - Static Sushi
# https://atcoder.jp/contests/abc095/tasks/arc096_b
# tag: 考察

# 時計回りにある程度食べ（食べなくてもいい）、引き返し、
# 逆に反時計回りに食べ進め、退店
# もしくは、その逆……という食べ方になる。

# スタート地点から、時計回りと反時計回りの両方のテーブルを作成していく。
# その際、i 番目の寿司まで食べ進んでそのまま出る場合と、
# いったんスタート地点まで引き返す場合の 2 種類を作成する。
# また、保持するのはそこまでに得できるカロリーの最大値とする。

# つまり、
# cw = clockwise, ccw = counter clockwiseとして、
# i 個目の寿司まで食べた時の得するカロリーの最大値
# cw_exit[i], cw_return[i], ccw_exit[i], cw_return[i]
# の 4 種類のテーブルを事前に作っておく。

# そこから、cw / ccw, exit / return を組み合わせ、最大値を
# 求めていく。
# 具体的には exit[i] + return[j] で、i + j = N となる
# 組み合わせを全探索する。

def main():
    N, C = map(int, input().split())
    sushis = [list(map(int, input().split())) for _ in range(N)]

    sushis.sort()

    # 時計回り
    cw_exit = [0]
    cw_return = [0]
    eaten = 0
    for d, v in sushis:
        eaten += v

        # そこで出るパターン
        gain = eaten - d
        cw_exit.append(max(cw_exit[-1], gain))

        # 引き返すパターン
        gain = eaten - 2 * d
        cw_return.append(max(cw_return[-1], gain))

    # 反時計回りも同様に
    ccw_exit = [0]
    ccw_return = [0]
    eaten = 0
    for d, v in sushis[::-1]:
        eaten += v
        d = C - d

        gain = eaten - d
        ccw_exit.append(max(ccw_exit[-1], gain))

        gain = eaten - 2 * d
        ccw_return.append(max(ccw_return[-1], gain))

    result = 0

    # i 個目まで食べて引き返す、というパターンを全探索
    for i in range(0, N):
        gain1 = cw_return[i] + ccw_exit[N-i]
        gain2 = ccw_return[i] + cw_exit[N-i]
        result = max(result, gain1, gain2)
    
    print(result)

main()
