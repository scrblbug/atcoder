# AtCoder Regular Contest 111 A - Simple Math 2
# https://atcoder.jp/contests/arc111/tasks/arc111_a
# tag: 整数 剰余 N進数 考察

# (10**N // M) % M を求める……のだが、
# N がとんでもなく大きいため、そのまま突っ込むと TLE になる。

# 式をよく見ると気づくのだが、実はこの式で求まるのは、
# 10**N を M 進数で表した時の下から二桁目の数字である。

# より具体的には、
# 仮に 'abcdef' で表される K 進数の数字があるとき、
# 'abcdef' // K = 'abcde' となり、
# 'abcde' % K = 'e' となる。

# 逆に言えば、下二桁の情報さえ分かればいいわけで、
# これは 10**N % (M*M) で求めることが出来る。
# これは、最小二乗法を用いることで O(log N) にて
# 計算可能。

def main():
    N, M = map(int, input().split())

    # 下二桁の情報を求める。
    # Pythonでは pow(N, divisor, mod) を用いると楽。
    remainder = pow(10, N, M**2)

    # 下二桁分 // M が求める数字となる。
    print(remainder // M)

main()
