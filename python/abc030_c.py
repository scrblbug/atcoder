# AtCoder Beginner Contest 030 C - 飛行機乗り
# https://atcoder.jp/contests/abc030/tasks/abc030_c
# リスト

# そこまで難しい問題ではないが、時間をループ変数として取ると
# 10^9 の制限によって時間切れになるので、飛行機の時刻表を
# そのまま使用し、時間を加算していく。
# また、時刻表をどこまで使用したかを保持しておかないと、
# いちいち最初から見直していくことになり、計算量が O(N^2)に
# なってしまうので注意。

def main():
    N, M = map(int, input().split())
    X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 0なら空港Aに、1なら空港Bにいるとする
    airport_now = 0

    # どこまで時刻表をチェックしたかを保持しておく。
    index_a = 0
    index_b = 0

    time = 0
    result = 0

    while True:
        # 現在の時刻で乗れるところまで時刻表を進める
        if airport_now == 0:
            while time > A[index_a]:
                index_a += 1
                # 時刻表が終了したら、ループを終わる
                if index_a >= len(A):
                    break
            # 進めきったら、飛行機に乗る
            else:
                time = A[index_a] + X
                airport_now = 1
                continue
            # while ～ else を利用した多重ループ脱出
            break
        # 以下同じ
        else:
            while time > B[index_b]:
                index_b += 1
                if index_b >= len(B):
                    break
            else:
                time = B[index_b] + Y
                airport_now = 0
                # B → A の移動で一往復なので、答えに1を足す
                result += 1
                continue
            break
    
    print(result)

main()
