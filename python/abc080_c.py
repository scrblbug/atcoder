# AtCoder Beginner Contest 080 C - Shopping Street
# https://atcoder.jp/contests/abc080/tasks/abc080_c
# tag: bit全探索 典型問題 joisinoお姉ちゃん

def main():
    N = int(input())
    # 各店舗のスケジュールの 0 1 列を二進数とみなして数値に変換しておく
    open = [int(input().replace(' ', ''), 2) for _ in range(N)]
    profit = [list(map(int, input().split())) for _ in range(N)]

    result = -10**10

    # bit全探索。自分の店を開ける時間帯を 1 とする。
    for status in range(1, 1<<10):
        tmp_r = 0

        for shop in range(N):
            # 各店舗のスケジュールとビット演算の & を取れば、
            # 残っているビットが重複している時間帯になる。
            dubbed = open[shop] & status

            # 残っているビットを数える。意外とこの書き方が早い。
            cnt = bin(dubbed).count('1')

            tmp_r += profit[shop][cnt]

        if tmp_r > result:
            result = tmp_r

    print(result)

main()
