# AtCoder Beginner Contest 197 C - ORXOR
# https://atcoder.jp/contests/abc197/tasks/abc197_c
# tag: bit全探索 ビット演算 数列 典型問題

# 1 <= N <= 20 の制約の中で、区間の分け方を考える。
# 各要素の間（最大 19 箇所）に仕切りを入れると考えると、
# 2^19 = 524288 通りなので、全探索でも十分間に合う。
# この手の ある or なし の組み合わせの全探索には、
# bit全探索を用いると便利。

def main():
    N = int(input())
    A = list(map(int, input().split()))

    result = 10**18
    for st in range(1<<(N-1)):
        # 各区切り方に対して、or と xor それぞれの変数を用意し、
        # 数列の順に計算していく
        ored = 0
        xored = 0
        for i, a in enumerate(A):
            # とりあえず現在の数字を or してやる
            ored |= a

            # 仕切りが来たら、いままで or してきたものを
            # xor し、or 用の変数をリセット
            if st>>i & 1:
                xored ^= ored
                ored = 0

        # 最後残っている or に注意
        xored ^= ored

        if xored < result:
            result = xored
    
    print(result)

main()


