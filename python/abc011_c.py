# AtCoder Beginner Contest 011 C - 123引き算
# https://atcoder.jp/contests/abc011/tasks/abc011_3
# tag: 貪欲法 典型問題 一人ゲーム

# 小難しいことを考えると難しくなる問題。
# N <= 300 なので素直に貪欲法で解き、最短手数が 100 以下に
# なるかどうか考えるほうが楽。

def main():
    N = int(input())
    ng_no = [int(input()) for _ in range(3)]

    # スタートがNGなら問答無用で失敗
    # 1 <= NG <= 300 なので、0 は考えなくて良い
    if N in ng_no:
        print('NO')
        return
    
    # 現在地、手数を管理する
    now = N
    turn = 0

    while now != 0:
        # 0 まで到達可能なら、0 へ行く
        if 1 <= now <= 3:
            turn += 1
            now = 0
        else:
            # 以下、進めるだけ進む
            if now - 3 not in ng_no:
                now -= 3
                turn += 1
            elif now - 2 not in ng_no:
                now -= 2
                turn += 1
            elif now - 1 not in ng_no:
                now -= 1
                turn += 1
            # 進めないなら失敗
            else:
                print('NO')
                return
    
    # 0 になったとき、100手以内ならOK
    if turn <= 100:
        print('YES')
    else:
        print('NO')

main()
