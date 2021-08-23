# AtCoder Beginner Contest 019 C - 高橋くんと魔法の箱
# https://atcoder.jp/contests/abc019/tasks/abc019_3
# tag: 考察 高橋君

# f(x) == f(2x) なので、
# x, 2x, 4x, 8x.... は全て同じ数字を返す。
# つまり、与えられた数字を割り切れるだけ 2 で割り続け、
# その最後の数字でまとめてやるといい。

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 既出の数字を set で管理する。
    appeared = set()

    result = 0

    for a in A:
        # 2 で割れるだけ割る。
        while a % 2 == 0:
            a //= 2

        # 既出でないなら答えに 1 加え、
        # 既出の数字セットに入れておく。
        if a not in appeared:
            result += 1
            appeared.add(a)

    print(result)

main()
