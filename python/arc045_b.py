# AtCoder Regular Contest 045 B - ドキドキデート大作戦高橋君
# https://atcoder.jp/contests/arc045/tasks/arc045_b
# tag: いもす法 累積和 区間判定
from bisect import bisect_left
def main():
    N, M = map(int, input().split())
    allocs = [list(map(int, input().split())) for _ in range(M)]

    # いもす法でそれぞれの部屋の掃除人数を求める
    diff = [0] * (N+2)

    for a, b in allocs:
        diff[a] += 1
        diff[b+1] -= 1
    
    # 部屋の掃除人数が 1 のところだけ記録していく
    rooms = []
    tmp = 0
    for n in diff:
        tmp += n
        if tmp == 1:
            rooms.append(1)
        else:
            rooms.append(0)

    # 掃除人数が 1 のところの累積和を求めておく
    csum_ones = []
    tmp = 0
    for n in rooms:
        tmp += n
        csum_ones.append(tmp)

    # 区間ごとに、さっき作成した累積和を用いて合計を求める。
    # 合計が 0 じゃなければ、一人しか掃除しない区間を
    # 含んでいることになる。
    result = []
    for q_no, (left, right) in enumerate(allocs, start=1):
        s = csum_ones[right] - csum_ones[left-1]
        if s == 0:
            result.append(q_no)
    
    print(len(result))
    for r in result:
        print(r)

main()
