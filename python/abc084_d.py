# AtCoder Beginner Contest D - 2017-like Number
# https://atcoder.jp/contests/abc084/tasks/abc084_d
# tag: 整数 素数 範囲参照 エラトステネスの篩 累積和

# まずは 2017 に似た数を確定させ、あとは
# 地道に（累積和を用いつつ）数える。

def main():
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]

    # まずはエラトステネスの篩を用いて素数を列挙しておく
    primep = [True] * 100001
    primep[0], primep[1] = False, False

    for i in range(2, 100001):
        if not primep[i]:
            continue
        for j in range(2*i, 100001, i):
            primep[j] = False

    primes = [n for n in range(100001) if primep[n]]

    # 素数のうち、2017 に似た数を出していき、
    # 個数の累積和を求めておく
    like_2017p = [0] * 100001
    for p in primes:
        if primep[(p + 1) // 2]:
            like_2017p[p] = 1
    
    csum = [0]
    for i in range(1, 100001):
        csum.append(csum[-1] + like_2017p[i])
    
    # あとはクエリに答えていくだけ
    for l, r in queries:
        print(csum[r] - csum[l-1])

main()
