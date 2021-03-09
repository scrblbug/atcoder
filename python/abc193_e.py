# AtCoder Beginner Contest 193 E - Oversleeping
# https://atcoder.jp/contests/abc193/tasks/abc193_e
# tag: 中国剰余定理

# x <= t < x + y (mod (2x + 2y))
# p <= t < p + q (mod (p + q))
# この二つの条件を同時に満たす t を求める
# y と q の値は十分に小さいので、全探索を行う

# 拡張ユークリッドの互除法を使用する
def gcd_by_ex_ea(a, b):
    if b == 0:
        return (1, 0, a)
    s, t, d = gcd_by_ex_ea(b, a % b)
    return (t, s - (a//b) * t, d)

# 中国剰余定理
def crt(a, p, b, q):
    y, z, d = gcd_by_ex_ea(p, q)
    if a % d != b % d:
        return None
    s = (b - a) // d
    return (a + p * s * y) % (p * q // d)

import math
def main():
    T = int(input())
    queries = [list(map(int, input().split())) for _ in range(T)]

    for x, y, p, q in queries:
        result = math.inf

        # x <= t1 < x+y, p <= t2 < p+q の全探索
        for t1 in range(x, x+y):
            for t2 in range(p, p+q):
                t = crt(t1, 2*x + 2*y, t2, p+q)
                if t != None and t < result:
                    result = t
        if result == math.inf:
            print('infinity')
        else:
            print(result)

main()
