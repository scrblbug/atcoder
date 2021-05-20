# AtCoder Beginners Contest 201 D - Game in Momotetsu World
# https://atcoder.jp/contests/abc201/tasks/abc201_d
# tag: 二人ゲーム グリッド DP 高橋君 青木君

def main():
    H, W = map(int, input().split())
    field = [input() for _ in range(H)]

    # マスごとの点数を持っておく
    score = [[0] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            score[h][w] = 1 if field[h][w] == '+' else -1

    # dp[h][w]: 
    # 現在 (h, w) にいるとき、そこからゴールへと向かう時に
    # 互いに最善を尽くした場合の点数差分。
    # 但し (h, w) で手番のプレイヤーを基準とする。
    dpt = [[-10**10] * W for _ in range(H)]
    dpt[-1][-1] = 0

    # ひとつ前の DP の場所、つまり次に進む場所の点数を足すが、
    # その場所の DP の値は、手番が入れ替わって
    # 相手の点数になるので、ひくことになる。
    for h in range(H-1, -1, -1):
        for w in range(W-1, -1, -1):
            if h < H-1:
                dpt[h][w] = max(dpt[h][w], score[h+1][w] - dpt[h+1][w])
            if w < W-1:
                dpt[h][w] = max(dpt[h][w], score[h][w+1] - dpt[h][w+1])

    if dpt[0][0] > 0:
        print('Takahashi')
    elif dpt[0][0] == 0:
        print('Draw')
    else:
        print('Aoki')

main()