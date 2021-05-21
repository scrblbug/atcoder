# AtCoder Beginner Contest 027 C - 倍々ゲーム
# https://atcoder.jp/contests/abc027/tasks/abc027_c
# tag: 二人ゲーム 整数 高橋君 青木君

# 自分が手番開始時に持っている数字 x が
# p <= x <= q であるためには、
# 前の順で相手の持っている数字 y が
# (p+1)//2 <= y <= (q+1)//2 - 1
# でなければならない。

# これを r <= y <= s と置くと、
# その前の順で自分が持っている数字 z が
# r//2 <= z <=  s//2 である必要がある。

# つまり、p <= x <= q であるためには、前回の自分の手番で
# ((p+1)//2)//2 <= y <= ((q+1)//2-1)//2 であればいい。

# 勝利条件は、自分の手番開始時の数字 x が N を越えている、
# つまり N+1 <= x <= N*2+1 と考えてよい。

# これを用いて上記の条件をたどり、1 を含んでいれば
# 最初に手番を行うプレイヤー'Takahashi'の勝ちとなる。

def main():
    N = int(input())

    # 数字の下限と上限を管理
    lower = N+1
    upper = 2*N+1

    while True:
        if lower <= 1 <= upper:
            print('Takahashi')
            return

        # 1 が範囲に含まれないまま終わる場合
        if upper == 0:
            print('Aoki')
            return

        lower = ((lower+1)//2)//2
        upper = ((upper+1)//2-1)//2
    
main()
