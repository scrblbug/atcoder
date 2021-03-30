# AtCoder Grand Contest 011 A - Airport Bus
# https://atcoder.jp/contests/agc011/tasks/agc011_a
# tag: 貪欲法

# 貪欲法を用いる。
# すなわち、客が怒り出す寸前に、乗せられるだけ乗せた
# バスを出すようにすればよい。

# あとはどのように実装するかだが、ここではまずは到着時間でソートし、
# 何人目の客が怒り出しそうかを管理しながら進めていくことにした。

def main():
    N, C, K = map(int, input().split())
    arrival = [int(input()) for _ in range(N)]
    arrival.sort()

    # 最初にバスを 1 台待たせているイメージ
    result = 1
    next_angry = 0

    for check in range(1, N):
        angry_time = arrival[next_angry] + K

        # バスが満員で次の客が乗れないなら、バスを出発＆もう1台用意
        if check - next_angry + 1 > C:
            result += 1
            next_angry = check
            continue

        # 次の客の到着までに客が怒り出すなら、バスを出発＆もう1台用意
        time_now = arrival[check]
        if angry_time < time_now:
            result += 1
            next_angry = check
            continue

    print(result)

main()
