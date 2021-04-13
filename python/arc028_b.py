# AtCoder Regular Contest 028 B - 特別賞
# https://atcoder.jp/contests/arc028/tasks/arc028_2
# tag: 優先度キュー 高橋君

# 以下大まかな流れ。
# まず点数の上位 K 人を入れ物に入れる。
# 一番年寄りの年齢を確認する。この人の順位が、最初の回答にもなる。
# 次の順位の人を順番に見ていき、年齢がより若い人が登場したら、
# その人を入れ物へ入れ、一番年寄りを入れ物から取り除き、
# 次に年寄りの人の年齢を確認する（ここで答えが変化する）。
# 以下繰り返し……みたいなイメージ。

# というわけで、優先度つきキューを用いると簡単に実装できそう。
# 実装では、一番年寄りはキューから pop して管理するので
# 入れ替えが終わった後のキューには、K-1 人入っている形になる。

from heapq import heappush, heappop, heapify
def main():
    N, K = map(int, input().split())
    ages = list(map(int, input().split()))

    # 出力するのは順位なので、年齢: 順位 の辞書をつくっておく
    age_to_rank = {age:rank for rank, age in enumerate(ages, start=1)}

    # K 個入った優先度つきキューを構成
    hq = [-n for n in ages[:K]]
    heapify(hq)

    # 最初の一人を求めておく。ついでに回答も出力。
    oldest = -heappop(hq)
    print(age_to_rank[oldest])

    # K+1 位から順番に見ていく
    for age in ages[K:]:
        # 若い人が出てきたら優先度つきキューを使って入れ替える
        if age < oldest:
            heappush(hq, -age)
            oldest = -heappop(hq)

        # 回答を出力
        print(age_to_rank[oldest])

main()
