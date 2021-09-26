# AtCoder Beginner Contest 179 E - Sequence Sum
# https://atcoder.jp/contests/abc179/tasks/abc179_e
# tag: 数列 整数 剰余 考察

# M の剰余は M 種類しかない。
# つまり、数列 A は必ず M+1 回以内で同じ数字が現れる。
# また、直前の項目によって次の項目が決定されることから、
# 同じ数字が現れた後は、前回と同じ並びがループすることになる。

# これを利用して、ループしている部分をまとめて計算する。

def main():
    N, X, M = map(int, input().split())

    A = [X]

    # 前回数字が現れたインデックスを、数字ごとに保持しておく。
    seen = [-1] * M
    seen[X] = 0

    # ループがどこから始まるかを確認する。
    idx = 0
    while True:
        idx += 1
        X = X**2 % M

        if seen[X] != -1:
            before_loop = seen[X]
            loop = A[seen[X]:]
            break
        else:
            A.append(X)
            seen[X] = idx

    # before_loop: ループが始まるまでの数列の要素数
    # loop: A[before_loop] 以降繰り返されるループ内容

    # 求める範囲が、ループに入る前までの場合。
    if N <= before_loop:
        result = sum(A[:N])

    # ループを含む場合。
    else:
        # とりあえずループ前の分を足してから考える。
        result = sum(A[:before_loop])
        N -= before_loop

        # ループの回数と余り回数を求め、それに応じた数列分の
        # 合計を加える。
        loop_n = N // len(loop)
        remain = N % len(loop)

        result += sum(loop) * loop_n
        result += sum(loop[:remain])

    print(result)

main()
