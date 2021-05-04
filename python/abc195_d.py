# AtCoder Beginner Contest 195 D - Shipping Center
# https://atcoder.jp/contests/abc195/tasks/abc195_d
# tag: 貪欲法

# N, M, Q の制約がゆるいので、愚直にやっていけば通る。

# 箱に入れていく際は、価値の大きいものから順番に、
# なるべく小さな箱に入れていく。

# 価値の大きな品物から順に入れていくとする。
# 今仮にある価値 V の品物を入れないという選択肢を
# 取ったとしても、一つの箱には一つしか品物を
# 入れられないので、それによって追加で入れることが
# できるようになる品物の価値は V 以下になってしまう。

# というわけで、貪欲法でいい。

def main():
    N, M, Q = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(N)]
    boxes = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(Q)]

    # 価値の大きい順に並べ替える
    items.sort(key=lambda x:-x[1])

    # クエリ順に処理
    for l, r in queries:
        # 使える箱を抽出し、小さい順に並べ、使用フラグを準備
        t_boxes = boxes[:l-1] + boxes[r:]
        t_boxes.sort()
        used = [False] * len(t_boxes)

        # 価値の大きいものから順に、入れ物に入れていく
        result = 0
        for w, v in items:
            # 愚直に小さい箱から順番に見ていく
            for i, cap in enumerate(t_boxes):
                # 入ったら used フラグを立て、次の品物へ
                if cap >= w and used[i] == False:
                    used[i] = True
                    result += v
                    break

        print(result)

main()
