# AtCoder Beginner Contest 161 F - Division or Subtraction
# https://atcoder.jp/contests/abc161/tasks/abc161_f
# tag: 整数 倍数 MOD

# 数字の変化を考えると、減算によって mod は変化しないことより、
# 一度減算に入ると割る操作に移行することはない。
# つまり、まず割り切れる間割り続け、次に減算が起こることになる。

# そこで、割り算が起こる場合と起こらない場合に分けて考える。
# 起こる場合は、当然 K の候補は N の約数に限定される。

# 起こらない場合は、N から K を減算し続けて 1 になるので、
# K は N-1 の約数である必要がある。

# そこで、N の約数と N-1 の約数を列挙し、これを全て
# 試してみる（一回一回は O(logN) なので大したことはない）
# ことで、回答可能。

def main():
    N = int(input())

    # 約数を set で管理
    divisor = set()

    # N の約数列挙
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            divisor.add(i)
            divisor.add(N // i)
    
    # (N-1) の約数列挙
    for i in range(1, int((N-1)**0.5)+1):
        if (N-1) % i == 0:
            divisor.add(i)
            divisor.add((N-1) // i)
    
    result = 0

    # 全部試し、条件が合うものを数える
    for d in divisor:
        tmp = N
        while d != 1 and tmp % d == 0:
            tmp //= d
        if tmp % d == 1:
            result += 1

    print(result)

main()
