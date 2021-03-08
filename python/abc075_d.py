# AtCoder Beginner Contest 075 D - Axis-Parallel Rectangle
# https://atcoder.jp/contests/abc075/tasks/abc075_d
# tag: 座標圧縮 累積和

# 座標の制限が -10^9 ～ 10^9 と広いため、そのまま空間を
# ループで探索しようとすると、計算量が大きくなりすぎる。
# そこで、点の数は 50 以下と少ないので、各点の x, y 座標と
# 一致するところだけを考えることにする。
# 最小面積を求める問題なので、間にある座標を考慮する必要は
# （幅 1 のケースを除けば）無い。

def main():
    N, K = map(int, input().split())
    points = [list(map(int, input().split())) for _ in range(N)]

    # 現れる x, y の数字を記録し、小さい順に数字を振っていく。
    pos_x = []
    pos_y = []
    for x, y in points:
        pos_x.append(x)
        pos_y.append(y)
    
    pos_x.sort()
    pos_y.sort()

    dict_x = {pos:comp for comp, pos in enumerate(pos_x)}
    dict_y = {pos:comp for comp, pos in enumerate(pos_y)}

    # 最終的に、x, y それぞれで何番目に現れる数字かという
    # 圧縮後の座標だけで考えていく
    c_points = [(dict_x[x], dict_y[y]) for x, y in points]

    # 点の数を素早く数えられるよう、二次元累積和を求めておく
    csum = [[0] * (len(pos_x) + 1) for _ in range(len(pos_y) + 1)]
    for x, y in c_points:
        csum[y+1][x+1] = 1
    
    for y in range(1, len(pos_y) + 1):
        tmp = 0
        for x in range(1, len(pos_x) + 1):
            tmp += csum[y][x]
            csum[y][x] = tmp
    
    for x in range(1, len(pos_x) + 1):
        tmp = 0
        for y in range(1, len(pos_y) + 1):
            tmp += csum[y][x]
            csum[y][x] = tmp
    
    # 指定された領域に含まれる点の数を返す関数
    def get_num_of_points(x1, x2, y1, y2):
        return csum[y2+1][x2+1] - csum[y2+1][x1] - csum[y1][x2+1] + csum[y1][x1]
    
    # 指定された領域の面積を返す。
    # ただし、幅を 1 取ってやることで細長い長方形にできるので
    # x1 == x2 や y1 == y2 のケースも考慮する。
    def get_area_of_rect(x1, x2, y1, y2):
        if x1 == x2:
            return pos_y[y2] - pos_y[y1]
        elif y1 == y2:
            return pos_x[x2] - pos_x[x1]
        else:
            return (pos_x[x2] - pos_x[x1]) * (pos_y[y2] - pos_y[y1])

    result = 10**20

    # 領域を全探索。 N^4 ループになる。
    for x1 in range(len(pos_x)-1):
        for x2 in range(x1, len(pos_x)):
            for y1 in range(len(pos_y)-1):
                for y2 in range(y1, len(pos_y)):
                    if get_num_of_points(x1, x2, y1, y2) >= K:
                        area = get_area_of_rect(x1, x2, y1, y2)
                        if area < result:
                            result = area
    print(result)

main()


