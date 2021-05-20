# AtCoder Beginner Contest 133 D - Rain Flows into Dams
# https://atcoder.jp/contests/abc133/tasks/abc133_d
# tag: 循環 考察

# 仮に 5 個ずつの山とダムで考えてみる。

#   山: a   b   c   d   e   (a)
# ダム:   p   q   r   s   t   (p)

# ここで、全体に降った雨の量は 
# a + b + c + d + e = p + q + r + s + t
# また、(b + c) / 2 = q, (d + e) / 2 = s
# よって、a + 2q + 2s = p + q + r + s + t
# よって、a = p - q + r - s + t
# a が決まると、(a + b) / 2 = p より、
# b = 2p - a
# 以下略

def main():
    N = int(input())
    A = list(map(int, input().split()))

    result = []

    # 奇数番目の合計から偶数番目の合計を引いたものが、
    # 山 1 に降った水の量となる
    result.append(sum(A[::2]) - sum(A[1::2]))

    # 以下考察に従って順番に山の降雨量を決めていく
    for a in A[:-1]:
        result.append(2 * a - result[-1])
    
    print(*result)

main()
