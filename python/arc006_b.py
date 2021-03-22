# AtCoder Regular Contest 006 B - あみだくじ
# https://atcoder.jp/contests/arc006/tasks/arc006_2
# tag: アスキーアート

# 与えられた文字列（アスキーアート）から情報を取り出し、
# それを元に処理を行う必要がある問題。
# 落ち着いて実装すれば、それほど難しくは無い、と思う。

def main():
    N, L = map(int, input().split())
    lottery = [input() for _ in range(L+1)]

    x_now = lottery[-1].find('o')
    width = 2 * N - 1

    # あみだくじを下から逆にたどっていく感じで……
    for y in range(L, -1, -1):
        # 現在地の右側に棒があれば x 座標に +2
        if x_now + 1 < width and lottery[y][x_now + 1] == '-':
            x_now += 2
        # 現在地の左側に棒があれば x 座標に -2
        elif x_now - 1 >= 0 and lottery[y][x_now - 1] == '-':
            x_now -= 2
    
    # x 座標を n 本目に変換して出力
    result = x_now // 2 + 1
    print(result)

main()
