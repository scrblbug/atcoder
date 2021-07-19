# AtCoder Regular Contest 017 B - 解像度が低い。
# https://atcoder.jp/contests/arc017/tasks/arc017_2
# tag: 数列 単調増加 連続部分列

# わかりやすさと書きやすさ重視で……
def main():
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]

    # 初項を1として、連続単調増加回数をカウントする
    seq = [1]
    for i in range(1, N):
        if A[i] > A[i-1]:
            seq.append(seq[-1] + 1)
        else:
            seq.append(1)

    # 連続増加回数 >= K となっている数が答え
    print(sum(s >= K for s in seq))

main()
