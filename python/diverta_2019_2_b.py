# diverta 2019 Programming Contest 2 B - Picking Up
# https://atcoder.jp/contests/diverta2019-2/tasks/diverta2019_2_b
# tag: コーナーケース 考察

# p, q を適切に選んだ時、最大で何手減らせるかを考える。
# そこで、全ての点の組み合わせの差分 (dx, dy) を確認し、
# 一番多い組み合わせを p, q にすればいい。

# ただしコーナーケースとして、点が元々一つしか無いときは
# 差分が存在しない。単純に 1 を出力して終了する。

def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]

    # コーナーケース
    if N == 1:
        print(1)
        return

    # 差分をカウントする
    diff_cnt = dict()

    # 全ての点の組み合わせを確認
    for i in range(N-1):
        x1, y1 = points[i]
        for j in range(i+1, N):
            x2, y2 = points[j]

            # 差分は (dx, dy) と (-dx, -dy) の
            # 二通りあるので、なんらかの基準で
            # 統一してやる必要がある。
            # ここでは、dx, dy の符号が違う場合は
            # dx を正に。そうでない場合はどちらも
            # 0 以上になるように合わせることにした。
            dx, dy = x1 - x2, y1 - y2
            if dx * dy < 0:
                dx = abs(dx)
                dy = -abs(dy)
            else:
                dx = abs(dx)
                dy = abs(dy)
            
            if (dx, dy) not in diff_cnt:
                diff_cnt[(dx, dy)] = 0
            diff_cnt[(dx, dy)] += 1

    # 同じ差分の組み合わせだけ手数を減らすことができる。
    print(N - max(diff_cnt.values()))

main()

