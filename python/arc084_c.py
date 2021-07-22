# AtCoder Regular Contest 084 C - Snuke Festival
# https://atcoder.jp/contests/arc084/tasks/arc084_a
# tag: 数え上げ すぬけ君 りんごさん

# 上部から順番に考えてしまうと、上部ごとに使える中部ごとに使える下部……
# といった感じで数える羽目になり、やや面倒くさいことになる。

# 中部から決定すると、上部と下部の数をすぐ決定できるので
# 解きやすい。

def main():
    N = int(input())
    tops = list(map(int, input().split()))
    mids = list(map(int, input().split()))
    bots = list(map(int, input().split()))

    # あとで探索する時用に番兵を追加しておく
    tops = sorted(tops) + [10**10]
    mids.sort()
    bots = sorted(bots) + [10**10]

    result = 0

    # 中央に応じて、上部と下部がどこまで使用可能かを順に見ていく
    top_idx = 0
    bot_idx = 0
    for mid in mids:
        # 上部 - 使えるものが増えていく
        # 使えなくなるところまで進める
        while tops[top_idx] < mid:
            top_idx += 1
        top_n = top_idx

        # 下部 - 使えるものが減っていく
        # 使えなくなるところまで進める
        while bots[bot_idx] <= mid:
            bot_idx += 1
        bot_n = N - bot_idx

        # 下部に使えるものが無くなったら終了していい
        if bot_n == 0:
            break

        # 使える上部の数 * 使える下部の数を答えに加える
        result += top_n * bot_n

    print(result)

main()

