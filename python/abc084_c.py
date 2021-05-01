# AtCoder Beginner Contest 084 C - Special Trains
# https://atcoder.jp/contests/abc084/tasks/abc084_c
# tag: 愚直

# 愚直にシミュレートしていけばいい。
# 駅についた時、次に乗れる電車がいつくるのかを判定する
# ところが、若干ややこしいかも。割った余りをうまく使っていこう

def main():
    N = int(input())
    stations = [list(map(int, input().split())) for _ in range(N-1)]

    # 今回はなんとなく再帰関数で書いてみた。なんとなく。
    # get_cost(駅番号, その駅への到着時間) = 駅 N に着く時間
    def get_cost(st, time):
        # 駅 N に着いたらその時間を返す(0-indexedなので注意)
        if st == N - 1:
            return time

        # 次に乗れる電車の時間を求める
        c, s, f = stations[st]

        # 始発までは待たないとダメ
        if time <= s:
            next_train = s
        else:
            # 前回の電車から何分遅れで到着？
            late = time % f

            # 電車の時間ぴったりなら、その電車に乗れる
            if late == 0:
                next_train = time

            # でなければ、次の電車
            else:
                next_train = time + f - late

        # 次の駅へ到着したとして再帰
        return get_cost(st+1, next_train + c)

    for i in range(N):
        print(get_cost(i, 0))

main()

