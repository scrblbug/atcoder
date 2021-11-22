# AtCoder Regular Contest 129 A - Smaller XOR
# https://atcoder.jp/contests/arc129/tasks/arc129_a
# tag: ビット演算 考察

# 二進数において、どの桁から x が N を下回るようになるかを、
# 上の桁から考えていく。

# 具体的に
# N: 101101 (= 45)
# の時を考えていく。

# x: 1xxxxx (32 <= x <= 63)
# のとき、xor を取ると
# n: 0xxxxx
# となるので、間違いなく下回る。

# x: 0xxxxx (x <= 31)
# のとき、xor を取っても下回るとは限らない。
# 次の桁を見る。

# x: 01xxxx (16 <= x= < 31)
# では、xor をとると
# n: 11xxxx となり、上回ってしまう。よって

# x: 00xxxx (x <= 15)
# として次の桁を見る……

# 以下同様に考察を進めると、
# N で i桁目が 1 の時は
# x の i桁目が 1 で条件を満たす。
# 0 の時は保留なので、この桁を 0 で確定して次の桁を見る。

# N で i桁目が 0 の時は
# x の i桁目が 1 ならかならず上回ってしまう。
# よって、この桁を 0 で確定して次の桁を見る。

# ところで、ここに加えて L, R も考察しなければならないが、
# 上の方の桁は全て 0 で確定されるので、考慮中の値の範囲は
# 簡単に求められる。
# それを L, R と比較してやればいい。

def main():
    N, L, R = map(int, input().split())
    result = 0

    # 下から i+1 桁目
    for i in range(63, -1, -1):
        # いま考慮される値の範囲
        now = 1<<i
        upper = now * 2 - 1
        lower = now

        # L, R の範囲と重ならない時の処理
        if upper < L:
            break
        elif R < lower:
            continue

        if N & now:
            result += min(R, upper) - max(L, lower) + 1
    
    print(result)

main()

