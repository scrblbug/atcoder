# AtCoder Beginner Contest 194 E - Mex Min
# https://atcoder.jp/contests/abc194/tasks/abc194_e
# tag: 数列 MEX 最小値 尺取法

# 最小値さえ求まればいいので、途中で
# 個数が 0 になる整数を列挙できればいい……
# という発想。

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 1 ～ N の個数をカウントするリスト
    cnt = [0] * (N+1)

    # 数列の最初の M 個については
    # 愚直に数え、MEX も愚直に探す。
    for a in A[:M]:
        cnt[a] += 1
    result = cnt.index(0)

    # ここから尺取法
    for i in range(N-M):
        addition = A[i+M]
        removal = A[i]

        # 追加される数字（右端）の個数を 1 増やす。
        cnt[addition] += 1

        # 削除される数字（左端）の個数を 1 減らす。
        cnt[removal] -= 1

        # 減らした後 0 個になっていれば、今の最小値と比較する。
        # ちなみに、 0 個になったとしても、同時に
        # もっと小さな数が 0 個である可能性もあるため、
        # そのタイミングでの MEX とは限らない。
        # しかし、求める最小値は必ず一度は 0 になるので、
        # 回答としては問題ない。
        if cnt[removal] == 0:
            if removal < result:
                result = removal
    
    print(result)

main()



