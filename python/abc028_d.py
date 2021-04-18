# AtCoder Beginner Contest 028 D - 乱数生成
# https://atcoder.jp/contests/abc028/tasks/abc028_d
# tag: 確率

# どちらかというと数学の問題。
# 真面目に確率を計算する。

def main():
    N, K = map(int, input().split())

    cnt = 0 

    # 1 < J < K < L < N となるような J, K, L が出るケース
    # 順番は 6 通り
    cnt += (K-1) * 1 * (N-K) * 6

    # 3 回中 2 回 K が出るケース
    # 順番は 3 通り
    cnt += 1 * 1 * (N-1) * 3

    # 3 回とも K が出るケース。これは 1 通りしか無い
    cnt += 1

    # 全パターンは N^3 なので、それで割る
    print(cnt / N**3)

main()
