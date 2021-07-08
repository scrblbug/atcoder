# AtCoder Beginner Contest 166 E - This Message Will Self-Destruct in 5s
# https://atcoder.jp/contests/abc166/tasks/abc166_e
# tag: 考察 順列・組み合わせ 数え上げ

# ある人物の番号を n, 身長を h とする。
# この人物とペアになり得る人の番号を m, 身長を g とすると、
# m - n = g + h, もしくは n - m = g + h
# よって、m - g = n + h もしくは m + g = n - h
# つまり、「番号と身長の和」と「番号と身長の差」が
# 等しい二人がペアになる。

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 番号 + 身長, 番号 - 身長別にそれぞれ
    # 何人いるのかをカウントする
    add = dict()
    sub = dict()

    for n, h in enumerate(A, start=1):
        if n+h not in add:
            add[n+h] = 0
        add[n+h] += 1

        if n-h not in sub:
            sub[n-h] = 0
        sub[n-h] += 1

    # 両方の辞書に同じ鍵があれば、その組み合わせ数を加算
    result = 0
    for key, value in add.items():
        if key in sub:
            result += value * sub[key]

    print(result)

main()
