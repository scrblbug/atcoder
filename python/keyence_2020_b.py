# キーエンスプログラミングコンテスト2020 B - Robot Arms
# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_b
# tag: 事前ソート 貪欲法 典型問題

# 区間が重ならないように、可能な限りたくさん配置を行う。
# スケジューリングなどの形で出てくることもある、典型問題。
# 解き方としては、区間の右側でソートを行い、貪欲に取っていけばいい。

def main():
    N = int(input())
    robots = [list(map(int, input().split())) for _ in range(N)]

    # 与えられたデータを区間データに変換
    arm_ranges = []
    for x, l in robots:
        arm_ranges.append((x-l, x+l))

    # 区間の右側でソート
    arm_ranges.sort(key=lambda x:x[1])

    result = 0

    # 現在取っている区間の右端を管理する
    now = -10**10

    for left, right in arm_ranges:
        # 貪欲法。取れるなら取り、現在地を区間の右に変更
        if left >= now:
            result += 1
            now = right

    print(result)

main()
