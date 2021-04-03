# AtCoder Regular Contest 042 A - 掲示板
# https://atcoder.jp/contests/arc042/tasks/arc042_a
# tag: 考察

# 投稿が行われたものは、行われていないものよりも前に来る。
# また、最後に投稿されたものほど前に来る。
# つまり、投稿が行われたものを時系列の逆順に並べ替えて出力し、
# その後に投稿が行われていないものを順に出力すればいい。

def main():
    N, M = map(int, input().split())
    post = [int(input()) for _ in range(M)]

    # 投稿が行われたものを、時系列の逆順に保存
    posted = []

    # 時系列の逆順に見ていく時、同じスレッドが二回以上現れた時は
    # 無視する必要があるため、出現したかどうかを管理しておく
    appeared = [False] * (N+1)

    for p in post[::-1]:
        if appeared[p] == True:
            continue
        posted.append(p)
        appeared[p] = True

    # 投稿が行われていないものを洗い出し
    others = [i for i in range(1, N+1) if appeared[i]==False]

    for t in posted:
        print(t)
    for t in others:
        print(t)

main()

