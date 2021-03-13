# AtCoder Beginner Contest 161 D - Lunlun Number
# https://atcoder.jp/contests/abc161/tasks/abc161_d
# tag: キュー

# とりあえずどんな感じなのか、最初の方を手書きで列挙してみる
# 1, 2, 3, 4, 5, 6, 7, 8, 9,
# 10, 11, 12, 21, 22, 23, ...., 87, 88, 89, 98, 99,
# 100, 101, 110, 111, 112, 121, 122, 123...

# 例えば 1 -> (10, 11, 12) や 11 -> (110, 111, 112) といった
# 構造があり、桁数が一つ少ないものから、次の桁数のものを
# 順次構成することが可能。

# そこで、両端キュー(deque)を用いて、
# まず一桁の数 1 ～ 9 を中に入れておき、FIFOで順に取り出しながら
# 二桁の数を構成していき、それをキューに入れていく。
# 二桁の数が順番に出てきだしたら、そこから三桁の数を
# 構成し……とやれば、小さな数から順に取り出していける。

from collections import deque
def main():
    K = int(input())
    dq = deque(list(range(1, 10)))
    cnt = 0
    while cnt < K:
        n = dq.popleft()
        # 最後の桁が 0 以外なら、abc から abc(c-1)を作成し、キューに入れる
        if n % 10 != 0:
            dq.append(n * 10 + n % 10 - 1)
        # abc から abcc を作成し、キューに入れる
        dq.append(n * 10 + n % 10)
        # 最後の桁が 9 以外なら、abc から abc(c+1)を作成し、キューに入れる
        if n % 10 != 9:
            dq.append(n * 10 + n % 10 + 1)
        cnt += 1
    
    print(n)

main()
