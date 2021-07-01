# AtCoder Beginner Contest 024 C - 民族大移動
# https://atcoder.jp/contests/abc024/tasks/abc024_c
# tag: 貪欲法 愚直 高橋王国

# 可能な限り目的の街に近づくように、貪欲に
# 移動させればいい。
# 民族の数: 1 <= K <= 100
# 大移動の日数: 1 <= D <= 10000
# より、愚直にシミュレートして十分間に合う。

def main():
    N, D, K = map(int, input().split())
    movable = [list(map(int, input().split())) for _ in range(D)]
    races = [list(map(int, input().split())) for _ in range(K)]

    # 民族ごとにシミュレートしていく
    for pos, goal in races:
        # 各移動日ごとの制限を見ていく
        for d, (left, right) in enumerate(movable,start=1):
            # 移動可能かどうかをチェック
            if not (left <= pos <= right):
                continue

            # この日にゴール可能なら、ゴールして次の民族へ
            if left <= goal <= right:
                print(d)
                break

            # ゴール可能でなければ、一番ゴールに近い街へ移動
            elif goal < left:
                pos = left
            else:
                pos = right

main()

