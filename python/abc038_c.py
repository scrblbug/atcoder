# AtCoder Beginner Contest 038 C - 単調増加
# https://atcoder.jp/contests/abc038/tasks/abc038_c
# 数列 考察 数え上げ

# 単調増加になる [l, r] の組み合わせ数を求める。
# 制約が 1 <= N <= 10^5 なので、[l, r] の全探索では間に合わない。
# が、ある最大の長さの部分単調増加列 [al, ..., ar] が存在する時、
# その中には要素数を N として、 (N+1) * N // 2 個の
# 単調増加列が存在することが分かる。
# （区間の左端と右端を、N 種類から 2 個 重複ありで選ぶ組み合わせ数）
# よって、端から順番に単調増加列を探していき、途切れたところで
# その中の組み合わせ数を足していけばいい。

def main():
    N = int(input())
    A  = list(map(int, input().split()))

    # 適当な初期値を設定してやる。
    # seq = 連続中の単調増加列の要素数
    # prev = 前回の数
    prev = 0
    seq = 0
    result = 0

    for a in A:
        # 単調増加が続いていれば、要素数に 1 足す
        if a > prev:
            seq += 1
            prev = a
        else:
        # 単調増加が途切れたところで、組み合わせ数を足して
        # 次の単調増加列をスタートさせる
            result += (seq + 1) * seq // 2
            prev = a
            seq = 1

    # 最後に残っている分を足してやること
    result += (seq + 1) * seq // 2

    print(result)

main()
