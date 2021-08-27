# AtCoder Regular Contest 034 B - 方程式
# https://atcoder.jp/contests/arc034/tasks/arc034_2
# 整数

# 1 <= N <= 10^18 なので、
# 1 <= f(x) <= 9 * 18 (= 162)

# よって、条件を満たしうる候補は、
# N - 162 ～ N - 1 の間にしか無い。

def main():
    N = int(input())

    # 各桁の合計と、自分自身の合計を返す関数。
    def func(x):
        return x + sum(int(c) for c in str(x))
    
    result = []

    # 候補となりうる数字を全探索する。
    for n in range(max(1, N - 162), N):
        # 候補が条件を満たすなら回答に追加。
        if func(n) == N:
            result.append(n)

    # 出力
    print(len(result))
    for r in result:
        print(r)

main()

