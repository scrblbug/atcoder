# AtCoder Beginner Contest 204 D - Cooking
# https://atcoder.jp/contests/abc204/tasks/abc204_d
# tag: 部分和 計算量 典型問題 高橋君

# 料理は好きな順番で作ることができる。
# つまり、オーブン 1 で作る料理と、 オーブン 2 で作る料理を
# なるべく時間が均等になるように分ける問題と考えることができる。

# 1 <= N <= 100, 1 <= Ti <= 1000 の制約より、
# 時間の部分和を求めていったとして、全て求めても 10^5 種類以下。
# というわけで、部分和としてあり得る組み合わせを全て列挙する。

def main():
    N = int(input())
    T = list(map(int, input().split()))

    # あらかじめ合計時間を出しておく。
    total = sum(T)

    # 公式解説では DP を用意して行っているが、
    # ここでは set を用いて、あり得る部分和を管理する。
    sums = set([0])
    for t in T:

        # 今回追加される部分和
        addition = set()

        for s in sums:
            # 総和の半分以下のものだけ使用する。
            if s + t <= total // 2:
                addition.add(s + t)

        # 前回の部分和の集合に、今回作成した集合を加える
        sums = sums | addition

    # 総和から部分和のうち最大のものを引いたのが答え
    result = total - max(sums)

    print(result)

main()
