# AtCoder Beginner Contest 216 E - Amusement Park
# https://atcoder.jp/contests/abc216/tasks/abc216_e
# tag: 考察 二分探索 高橋君 コーナーケース

# 楽しさが一番大きいものに乗り続けるのが最善。
# 1 <= K <= 2*10^9 という制約から、愚直にシミュレートすると
# 間に合わない。

# 楽しさが大きいものから順に p, q, r, s ... とする。
# 乗る回数が大きくなると、最終的にはある閾値 t で切られたような
# 形になるはずである。すなわち、
# 楽しさ
# t = (p - a) : a 回乗っている
# t = (q - b) : b 回乗っている
# r (< t) : まだ乗っていない
# s (< t) : まだ乗っていない

# そこで、ある楽しさ t まで全ての乗り物に
# 乗り続けたとして、合計何回乗ることになるのかを求める。
# その回数を n としたとき、n >= K となる最大の楽しさ maxt を
# 求める。（二分探索）
# その時に得られる楽しさの合計値から、あまっている回数
# (n - K) 分の maxt を引けば、それが回答になる……はず。

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 楽しさ threshold 以上の全ての乗り物に乗ったとき、
    # 乗ることになる回数を求める関数。
    def get_ride_count(threshold):
        return sum(max(0, a - threshold + 1) for a in A)
    
    # 二分探索。
    # 少なくとも楽しさ left の乗り物に一回は乗らなければならない
    # ような、left を求める。
    left = 0
    right = 10**10
    while right - left > 1:
        mid = (right + left) // 2
        if get_ride_count(mid) < K:
            right = mid
        else:
            left = mid

    ride_count = get_ride_count(left)

    # 改めて乗りものの楽しさの最低値と、
    # 乗りすぎている回数を求めておく。
    # left == 0 ならコーナーケース。
    # 全ての乗り物が楽しさ 0 になるまで乗ることになる。
    if left == 0:
        min_pleasure = 1
        remain = 0
    else:
        min_pleasure = left
        remain = ride_count - K

    # 改めて、楽しさを合計していく。
    result = 0
    for a in A:
        if min_pleasure > a:
            continue
        result += ((a + min_pleasure) * (a - min_pleasure + 1)) // 2

    # 余ってしまった回数分の楽しさを引く。
    result -= min_pleasure * remain

    print(result)

main()



