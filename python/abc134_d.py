# AtCoder Beginner Contest 134 D - Preparing Boxes
# https://atcoder.jp/contests/abc134/tasks/abc134_d
# tag: 考察

# i 個目の箱の中身を決定するに当たっては、
# i*2, i*3, i*4... 個目の箱の中身が決定している必要がある。
# 逆にいうと、右端から順番に箱の中身を決定していけばいい。

# 公式解説にもあるが、計算量を N + N//2 + N//3 + .... とした場合、
# 全体で O(N logN) となるので、計算量については安心していい。
# ちなみに、実際 10^5 で計算してみると 1166750 = 10^5 * 11.675 程度。

def main():
    N = int(input())
    # 1-indexed に合わせて初期化する
    cond = [0] + list(map(int, input().split()))
    boxes = [0] * (N+1)

    # now 個目の箱の中身を決める
    for now in range(N, 0, -1):
        cnt = 0
        # now*2, now*3... 個目の箱の中身を確認し、
        # 入っている玉の個数を求める
        for mult in range(now*2, N+1, now):
            cnt += boxes[mult]

        # 条件に一致していなければ、now 個目の箱に玉を入れる
        # （入れれば条件に一致するようになる）
        if cnt % 2 == cond[now]:
            boxes[now] = 0
        else:
            boxes[now] =1

    # 玉が入っている箱だけ抜き出す
    result = [i for i in range(1, N+1) if boxes[i]==1]

    print(len(result))
    if result:
        print(*result)

main()
