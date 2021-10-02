# AtCoder Beginner Contest 001 C - 風力観測
# https://atcoder.jp/contests/abc001/tasks/abc001_3
# tag: 誤差 愚直

# 割と愚直にやっていくだけ。
# 小数誤差を回避する一番簡単な方法は、
# 整数のまま比較してやること。

from bisect import bisect_right
def main():
    deg ,dis = map(int, input().split())

    dirs = [
        'N', 'NNE', 'NE', 'ENE',
        'E', 'ESE', 'SE', 'SSE',
        'S', 'SSW', 'SW', 'WSW',
        'W', 'WNW', 'NW', 'NNW'
    ]

    wind_dir = dirs[((deg+112) // 225) % 16]

    # 境界値は、予め 0.05 を引いて 60 を掛けてやるような形にする。
    # 最初から最後まで整数で取り扱うこと。
    dat = [
        0, 3, 16, 34, 55, 80, 108, 139, 172, 208, 245, 285, 327
    ]
    thresholds = [(v*10 - 5) * 6 // 10 for v in dat]

    wind_class = bisect_right(thresholds, dis) - 1

    if wind_class == 0:
        wind_dir = 'C'

    print(wind_dir, wind_class)

main()
