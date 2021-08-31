# Tenka1 Programmer Contest C - 4/N
# https://atcoder.jp/contests/tenka1-2017/tasks/tenka1_2017_c
# tag: 考察

# 4 / N = 1/h + 1/n + 1/w

# 両辺に hnw を掛けて移項
# 4hnw = Nnw + Nwh + Nhn
# 4hnw - Nnw - Nhn = Nwh

# n でまとめて
# n(4hw - Nw - Nh) = Nwh

# よって、
# n = Nwh / (4hw - Nw - Nh)

# h, w を全探索し、整数になる n を求めればいい。

def main():
    N = int(input())

    for h in range(1, 3501):
        for w in range(1, 3501):
            # n > 0 なので、4hw - Nw - Nh > 0
            if 4*h*w - N*w - N*h > 0 and N*w*h % (4*h*w - N*w - N*h) == 0:
                n = N*w*h // (4*h*w - N*w - N*h)
                print(h, n, w)
                return

main()
