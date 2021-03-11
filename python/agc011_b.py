# AtCoder Grand Contest 011 B - Colorful Creatures
# https://atcoder.jp/contests/agc011/tasks/agc011_b
# tag: 累積和

# 小さいものから順番に、ひとつ上の大きなものを吸収させていき、
# 吸収できなくなれば一旦ストップ・次のものを最初にして
# 再スタート。最後まで行き着くことができれば、
# スタートしたところ～最後のどの色にもなることができる……みたいな。

# 吸収できるかどうかはそれまでに吸収したもの全ての大きさの
# 合計が関わってくるので、累積和を使用する。
def main():
    N = int(input())
    A = list(map(int, input().split()))

    # ソートして累積和を取る
    A.sort()
    csum = []
    tmp = 0
    for a in A:
        tmp += a
        csum.append(tmp)

    start = 0
    now = 1
    while True:
        if now == N:
            break
        # 一つ前までの合計で、今考慮している生物を吸収可能かどうか
        if csum[now - 1] * 2 >= A[now]:
            now += 1
        else:
            start = now
            now += 1
    
    print(N - start)

main()
