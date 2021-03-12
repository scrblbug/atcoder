# AtCoder Grand Contest 041 B - Voting Judges
# https://atcoder.jp/contests/agc041/tasks/agc041_b
# tag: 二分探索

# ある点数の問題が採用可能かどうかのみを考えていく。
# これが求まれば、二分探索で、何点の問題までが採用可能なのかを
# 確認することで、全体の答えが求まる。
# そこで、ある点数の問題がギリギリ採用可能な投票の状況を考えていく。
from collections import Counter
def main():
    N, M, V, P = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    # ギリギリ通過すればいいので、上位 P-1 問はあらかじめ除いて
    # 点数分布を作成しておく
    # A[:-(P-1)] とすると P=1 のときおかしくなるので注意
    cnt = Counter(A[:N-(P-1)])

    # 点数をソートし、インデックスで管理
    scores = sorted(cnt.keys())

    # 二分探索チェック用関数
    def check(idx):
        # ギリギリの投票状況のときの点数ボーダーを考える。
        # 他の（上位P-1問を除く）すべての問題について、
        # このボーダーまでは投票可能として、その時の
        # 投票数をカウントしてみる
        border = scores[idx] + M

        # 上位 P-1 問には、全員が投票する
        votes = (P-1) * M

        # 他の問題に対する投票行動について考慮する。
        # 点数がボーダーになるまでは投票可能
        for s, n in cnt.items():
            # そもそもボーダーを越えるなら、Falseを返す
            if s > border:
                return False
            # チェック中の問題以下の点数の問題には、全員が投票
            elif s <= scores[idx]:
                votes += M * n
            # それ以外は、ボーダーまで投票
            else:
                votes += (border - s) * n
        
        # 実際の投票数 (M * V) が上記の投票数の合計を上回っている場合、
        # 票が上位にあふれてしまい、チェック中の問題は採用されなくなる
        if votes >= M * V:
            return True
        else:
            return False

    # low: 採用されない high: 採用される
    low = -1
    high = len(scores) - 1
    while high - low > 1:
        mid = (high + low) // 2
        if check(mid):
            high = mid
        else:
            low = mid

    # scores[high]以上の点数の問題なら採用可能性あり。
    # P-1 問をあらかじめ除いているのを足しておく
    result = sum(cnt[k] for k in cnt if k >= scores[high]) + (P-1)
    print(result)

main()
