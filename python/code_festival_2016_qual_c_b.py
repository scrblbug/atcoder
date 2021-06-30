# CODE FESTIVAL 2016 qual C B - K個のケーキ
# https://atcoder.jp/contests/code-festival-2016-qualc/tasks/codefestival_2016_qualC_b
# tag: 考察 高橋君

# どのような状況だと同じケーキを2日連続で食べなければ
# ならないのかを考察する。当然、あるケーキが多すぎれば
# 連続で食べなければならなくなる。

# そこで、もっとも多い数のケーキを A 、それ以外のケーキを B と
# まとめて考えてみる。

# 基本的には ABAB ... と食べていくことになるが、
# B を使い切ってなお残っている A を連続で食べる必要がある。

# 逆に、B の前に A が無くなる場合は、同じケーキを連続で
# 食べずに食べきることができる。（具体的には、一番多く残っている
# ケーキと次に多く残っているケーキを交互に食べていけばいい）

def main():
    K, T = map(int, input().split())
    cake_cnt = list(map(int, input().split()))

    max_n = max(cake_cnt)

    # 連続で同じケーキを食べる日数
    seq = max(0, (max_n - (K - max_n)))

    # 回答（前日と同じケーキを食べる日数）を出力
    if seq > 1:
        print(seq - 1)
    else:
        print(0)

main()