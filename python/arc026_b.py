# AtCoder Regular Contest 026 B - 完全数
# https://atcoder.jp/contests/arc026/tasks/arc026_2
# tag: 整数 完全数 約数 約数列挙 コーナーケース 高橋君

# 約数を列挙し、合計して確認するだけ……
# なのだが、実は 1で割るときの処理を間違うとコーナーケースに
# 引っかかる。(N=1)

# ここでは、素直に全約数を足し合わせた後、自分自身の分を
# 引いている。

def main():
    N = int(input())

    # 約数を列挙しながら足していく。
    sum_div = 0
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            sum_div += i
            if i ** 2 != N:
                sum_div += N // i

    # 自分自身は除く。
    sum_div -= N

    if sum_div < N:
        print('Deficient')
    elif sum_div == N:
        print('Perfect')
    else:
        print('Abundant')

main()
