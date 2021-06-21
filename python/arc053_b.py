# AtCoder Regular Contest 053 B - 回文分割
# https://atcoder.jp/contests/arc053/tasks/arc053_b
# tag: 文字列 回文 分割 高橋君

# ある文字が偶数個ある時は、回文の両側に自由に配置できるが、
# 奇数個の場合には 1 個余ってしまう ＝ 中央に置く必要がある。
# よって、奇数個の文字の種類だけの回文を作る必要がある。

from collections import Counter
def main():
    S = input()
    cnt = Counter(S)

    # 回文の中央に置く文字の数 ＝ 奇数個の文字の種類数
    palin_n = sum(n % 2 == 1 for n in cnt.values())

    # 中央以外に使用される文字のペア数
    pair_n = (sum(cnt.values()) - palin_n) // 2

    # 全て偶数個の場合（コーナーケース）
    if palin_n == 0:
        print(pair_n * 2)

    # 回文の数に分割し、文字数を求める
    else:
        print((pair_n // palin_n) * 2 + 1)

main()
