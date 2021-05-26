# AtCoder Grand Contest 038 A - 01 Matrix
# https://atcoder.jp/contests/agc038/tasks/agc038_a
# tag: グリッド 考察 特殊構造

# こういう感じで作ると条件を満たす

# H, W, A, B = 7, 7, 2, 3
# 0011111
# 0011111
# 0011111
# 1100000
# 1100000
# 1100000
# 1100000

def main():
    H, W, A, B = map(int, input().split())

    for i in range(B):
        print('0'*A + '1'*(W-A))
    for i in range(H-B):
        print('1'*A + '0'*(W-A))

main()
