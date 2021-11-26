# CODE FESTIVAL 2016 Final B - Exactly N points
# https://atcoder.jp/contests/cf16-final/tasks/codefestival_2016_final_b
# tag: 最小の最大値 二分探索 考察 高橋君

# 解いた問題の最大点が X 点の時、何点まで取れるかを
# 考えてみる。当然、その最大値は 1 ～ X 点の問題を
# 全て解いたもの、つまり (1 + X) * X // 2 点になる。

# 逆に、X 点の問題を入れた組み合わせなら、
# 適当な問題を一つ外すことで (1 + X) * X // 2 点までの
# 好きな組み合わせを作ることが可能。

# 念の為に具体例：
# 求めた最小の最大点数が 5 だとすると、
# (1, 2, 3, 4, 5) の問題セットになるが、
# これから 1, 2, 3, 4 のどれか一つを外し、
# 11 ~ 15 点の好きな点数を作成できる。
# また、10 点以下の場合は最小の最大点数は
# 4 以下になるので考慮しなくていい。

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
    # これは、1 から順番に足していき、N を越えた時、
    # つまり先ほど求めた最大点数まで足した時に、
    # N を越えている分ということになる。
    fault = (1 + max_point) * max_point // 2 - N

    result = [n for n in range(1, max_point+1) if n != fault]

    for r in result:
        print(r)

main()
