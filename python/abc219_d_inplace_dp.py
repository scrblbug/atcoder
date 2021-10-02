# 配列を使い回すDPは以下のような感じ。
# こちらの方が、使用メモリも速度も効率は良くなる。

def main():
    N = int(input())
    X, Y = map(int, input().split())
    boxes = [list(map(int, input().split())) for _ in range(N)]

    dpt = [[-1] * (Y+1) for _ in range(X+1)]
    dpt[0][0] = 0

    # 使い回す際は、後ろからループを回す。
    # ちなみに前から回した場合は、同じものをいくつでも入手可能
    # というパターンになる。
    for a, b in boxes:
        for tk in range(X, -1, -1):
            for ti in range(Y, -1, -1):
                if dpt[tk][ti] == -1:
                    continue
                new_tk = min(X, tk + a)
                new_ti = min(Y, ti + b)
                if dpt[new_tk][new_ti] == -1 or dpt[new_tk][new_ti] > dpt[tk][ti] + 1:
                    dpt[new_tk][new_ti] = dpt[tk][ti] + 1

    print(dpt[X][Y])

main()
