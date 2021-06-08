# AtCoder Beginner Contest 203 E - White Pawn
# https://atcoder.jp/contests/abc203/tasks/abc203_e
# tag: グリッド 考察 座標圧縮

# まず、1 <= N <= 10^9 という制限なので、
# そのまま y 座標をスキャンするのは厳しい。

# しかし、1 <= M <= 2 * 10^5 なので、y 座標は多くても
# 2*10^5 種類。つまり、y 座標の圧縮を行うことにする。

# 白ポーンが現在いられる x 座標をどんどん更新していく。
# その際、黒ポーンがいる x 座標を
# 1) 基本的にそのまま通過はできない
# 2) が、隣の x 座標にいる場合は移動してくることができる
# と考えるとやりやすい。

def main():
    N, M = map(int, input().split())
    blacks = [list(map(int, input().split())) for _ in range(M)]

    # 使用されている y 座標のみを保存する圧縮用リスト
    y_comp = []

    # y 座標ごとの黒ポーンの x 座標のリストを作成
    black_dic = dict()
    for y, x in blacks:
        if y not in black_dic:
            black_dic[y] = []
            # 新たな y 座標が現れた時に、圧縮用リストに追加
            y_comp.append(y)
        black_dic[y].append(x)

    # y 座標を小さい順に見ていく
    y_comp.sort()

    # 白ポーンが到達できる x 座標を管理。
    # set を使用することで、後の x-1 in x_set などを
    # 素早く判定できる
    x_set = set([N])

    for y in y_comp:
        # まず、隣の x 座標にいられるかどうかをチェックし、
        # 追加用リストを作成しておく。
        x_add = []
        for x in black_dic[y]:
            if x-1 in x_set or x+1 in x_set:
                x_add.append(x)

        # 条件 1 に基づき、黒ポーンの x 座標を削除
        for x in black_dic[y]:
            if x in x_set:
                x_set.remove(x)
        
        # 条件 2 に基づき、条件の合う黒ポーンの x 座標を追加
        for x in x_add:
            x_set.add(x)

    print(len(x_set))

main()
