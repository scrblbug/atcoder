# AtCoder Beginner Contest 123 D - Cake 123
# https://atcoder.jp/contests/abc123/tasks/abc123_d
# tag: 枝刈り

# A, B, C を降順にソートしておく。
# すると、A の a 番目、B の b 番目、 C の c 番目のケーキを
# 使用する場合、この組み合わせ以上の美味しさの組み合わせは、
# 少なくとも a * b * c 種類存在する。
# 逆にいうと、この組み合わせの順位は 最大でも a * b * c となる。
# K の最大値は3000なので、枝刈り全探索を用いて
# a * b * c <= K の範囲を全探索し、それぞれの美味しさを求める。
# ちなみにこの組み合わせ数は、11万通りほどなので、十分間に合う。

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # A, B, C をあらかじめ降順にソート
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    # 候補を格納していくリスト
    candies = []

    # 枝刈りしつつ全探索
    for a in range(1, X+1):
        if a > K:
            break
        for b in range(1, Y+1):
            if a * b > K:
                break
            for c in range(1, Z+1):
                if a * b * c > K:
                    break
                candies.append(A[a-1] + B[b-1] + C[c-1])
    
    # 候補をソートした上で上位から出力
    candies.sort(reverse=True)
    for i in range(K):
        print(candies[i])

main()
