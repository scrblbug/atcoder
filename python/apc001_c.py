# AtCoder Petrozavodsk Contest 001 C - Vacant Seat
# https://atcoder.jp/contests/apc001/tasks/apc001_c
# tag: 二分探索 インタラクティブ

# まず 0 と N-1 の席を探索し、これを両端として考える。
# 途中の席 X を探索し、これが 0 と同じ性別だったと仮定すると、

# 0 ～ X の席の数が偶数なら、席が全て埋まっていれば
# 矛盾が生じるので、0 ～ X 間のどこかに空席が存在する。

# 0 ～ X の席の数が奇数なら、X ～ N-1 の席の数は同じく奇数だが、
# N-1 と X の性別が違っているので、X ～ N-1 のどこかに
# 空席が存在する。

# 0 と X の性別が違う場合も、同様に空席が存在する区間をどちらかに
# 決定できる。

# ……といった感じで、二分探索の要領で区間を狭めていけば、
# いずれ空席を見つけることができる。

def main():
    N = int(input())

    # 席の状況を記録 0: 男性 1: 女性
    seats = [-1] * N

    # 席の状況を確認する関数。
    def ask(num):
        # flush=True と指定すると、出力バッファをフラッシュできる。
        print(num, flush=True)
        s = input()
        if s == 'Male':
            seats[num] = 0
        elif s == 'Female':
            seats[num] = 1
        else:
            exit()

    ask(0)
    ask(N-1)

    upper = N-1
    lower = 0
    while True:
        mid = (upper + lower) // 2
        ask(mid)
        if seats[lower] == seats[mid]:
            # 性別が同じで、席数が偶数なら、そちらに空席
            if (mid - lower + 1) % 2 == 0:
                upper = mid
            else:
                lower = mid
        else:
            # 性別が違って、席数が偶数なら、反対に空席
            if (mid - lower + 1) % 2 == 0:
                lower = mid
            else:
                upper = mid

main()
