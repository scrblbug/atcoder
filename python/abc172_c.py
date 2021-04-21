# AtCoder Beginner Contest 172 C - Tsundoku
# https://atcoder.jp/contests/abc172/tasks/abc172_c
# tag: 累積和 二分探索

# A の上から a 冊、B の上から b 冊を読むとする。
# a を全探索することを考え、一旦固定して考えてみる。
# つまり、b の最大値を答える問題を考える。

# これを素直に毎回イチから計算してしまうと、
# 計算量が O(NM) となり、間に合わない。

# ところで、a を単調増加に取ると、b の最大値は当然単調減少になる。
# つまり、前回の最大値から下を見ていき、丁度条件を満たすようになる
# ところまで値を下げればいい。
# この方法だと、a が 0 <= a <= N の範囲で動かされる間、
# b もちょうど N >= b >= 0 の範囲で動かされることになる。
# よって計算量は O(N+M) となり、間に合う。

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # イチイチ足したり引いたりするのはめんどくさいので、
    # 累積和を取っておくことにする。
    # これで a 冊, b 冊読むときの合計時間は
    # それぞれ csum_a[a], csum_b[b] で出せる。
    tmp = 0
    csum_a = [0]
    for t in A:
        tmp += t
        csum_a.append(tmp)
    tmp = 0
    csum_b = [0]
    for t in B:
        tmp += t
        csum_b.append(tmp)

    result = 0

    # b は後ろから、a は前から見ていく
    b = M
    for a in range(N+1):
        # a 冊だけで制限時間を越える場合は、探索を終了する
        if csum_a[a] > K:
            break

        # b を、条件を満たすところまで下げる
        while csum_b[b] + csum_a[a] > K:
            b -= 1

        # 合計で a + b 冊読めるので、最大値と比較
        if a + b > result:
            result = a + b
    
    print(result)

main()

# あらかじめ累積和を取っておき、そこを
# 二分探索することで、固定した a に対する b の上限を
# 素早く求めていくというやり方も可能。 O(N logM)
# ……というか、実はこっちを先に思いついたんだったり……。

from bisect import bisect_right
def main2():
    N, M, K = map(int, input().split())

    # A から 1 冊も本を読まない場合もあるので、
    # あらかじめ 0 分の本を最初に置いておく
    A = [0] + list(map(int, input().split()))

    B = list(map(int, input().split()))

    # 累積和を取っておく
    csum_b = []
    tmp = 0
    for t in B:
        tmp += t
        csum_b.append(tmp)

    result = 0

    # A に使う時間を更新しながら、それぞれの b の最大値を求めていく
    time_a = 0

    # A の最初は 0 冊目の 0 分の本とする
    for a, time in enumerate(A, start=0):
        time_a += time

        # A の本だけで制限時間を越えるようになったら break
        if time_a > K:
            break
        
        # B 用に使える時間の上限を計算し、
        # 二分探索関数で B の累積和リストのどこに入れられるかを
        # 確認する（これが b の最大値となる）
        time_b = K - time_a
        b = bisect_right(csum_b, time_b)

        if a + b > result:
            result = a + b
    
    print(result)

# main2()

