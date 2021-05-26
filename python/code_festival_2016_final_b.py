# CODE FESTIVAL 2016 Final B - Exactly N points
# https://atcoder.jp/contests/cf16-final/tasks/codefestival_2016_final_b
# tag: 最大の最小 二分探索 考察

# 解いた問題の最大点が X 点の時、何点まで取れるかを
# 考えてみる。当然、その最大値は 1 ～ X 点の問題を
# 全て解いたもの、つまり (1 + X) * X // 2 点になる。

# 逆に、X 点の問題を入れた組み合わせなら、
# X ～ (1 + X) * X // 2 点の組み合わせを作ることが
# 可能になる（適当な問題を不正解にすれば良い）。

def main():
    N = int(input())

    # まず、最小の最大点数を求めるが、
    # せっかくなので二分探索する
    left = 0
    right = N
    while right - left > 1:
        mid = (right + left) // 2
        if (1 + mid) * mid // 2 >= N:
            right = mid
        else:
            left = mid

    max_point = right

    # 引かなければならない点数を求める。
    # これは、1 から順番に足していき、N を越えた時に
    # N を越えている分ということになる。
    fault = (1 + max_point) * max_point // 2 - N

    result = [n for n in range(1, max_point+1) if n != fault]

    for r in result:
        print(r)

main()
