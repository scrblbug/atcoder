# 競プロ典型90問 011 - Gravy Jobs
# https://atcoder.jp/contests/typical90/tasks/typical90_k
# tag: 区間スケジューリング DP 事前ソート

def main():
    N = int(input())
    jobs = [list(map(int, input().split())) for _ in range(N)]

    # あらかじめ締め切り順にソートしておく
    jobs.sort(key=lambda x:x[0])
    max_day = jobs[-1][0]

    # dpt[i][j]:
    # 現在 i 個目の仕事を考慮している j 日目の朝 (0-indexed)
    dpt = [[0] * (max_day+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(max_day+1):
            deadend, cost, profit = jobs[i]
            deadend -= 1

            # 日程だけを進める場合
            if j > 0:
                dpt[i][j] = max(dpt[i][j], dpt[i][j-1])

            # i 個目の仕事をしない場合
            dpt[i+1][j] = max(dpt[i+1][j], dpt[i][j])

            # 仕事を締め切り内に終えられるなら、該当箇所を処理
            if j + cost - 1 <= deadend:
                dpt[i+1][j+cost] = max(dpt[i+1][j+cost], dpt[i][j] + profit)

    print(dpt[-1][-1])

main()
