# AtCoder Beginner Contest 099 C - Strange Bank
# https://atcoder.jp/contests/abc099/tasks/abc099_c
# tag: N進数

# 6 進数と 9 進数の組み合わせを考える問題。
# 幸い 1 <= N <= 100000 と制約が緩いので、
# 6 進数で数える分と 9 進数で数える分をわけることにして、全探索する。

def main():
    N = int(input())

    # ある数 x を p 進法で考えたときの
    # 各桁の数字の合計を返す関数を作成しておく。
    def get_op_num(x, p):
        result = 0
        while x:
            result += x % p
            x //= p
        return result

    result = N
    # 9 進法で数える分を 0 ～ N の範囲で動かし、全探索を行う。
    # 1 円の桁はどちらで数えても同じなので、9 の倍数だけ調べていく。
    for p_nine in range(0, N+1, 9):
        tmp = get_op_num(p_nine, 9) + get_op_num(N - p_nine, 6)
        if result > tmp:
            result = tmp
    
    print(result)

main()
