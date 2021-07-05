# AtCoder Regular Contest C - 積み重ね
# https://atcoder.jp/contests/arc006/tasks/arc006_3
# tag: 考察 高橋君

# 最終的な山の数＆山の一番上にある荷物だけを考慮すると考えやすい。

# ある荷物を置く際、他の荷物に積み重ねることが出来るなら、
# 積み重ねてしまっても構わない。
# なぜなら、今回仮に積まなかったとして、後から同じ場所に他の
# 荷物を積み重ねることにしたとしても、最終的な山の数と山の一番上に
# ある荷物は同じになるため。

# ただし、積み重ねる先の候補が複数ある場合は、なるべく大きな
# 荷物を一番上に残したいので、一番小さな荷物に積み重ねる必要がある。

# 制約は 1 <= N <= 50 と緩いので、適当に書いても大丈夫。

def main():
    N = int(input())
    boxes = [int(input()) for _ in range(N)]

    # 山の一番上だけを記録
    piles = []

    # 箱を順番に見ていく
    for w in boxes:

        # 現在の候補の山の場所と、一番上の大きさを初期化。
        min_pos = -1
        min_t = 10**10

        # 乗せられる山で、一番上が最も大きなものを探す
        for i, top in enumerate(piles):
            if w <= top < min_t:
                min_t = top
                min_pos = i
        
        # 乗せられる山がなければ、新たな山を追加
        if min_pos == -1:
            piles.append(w)
        
        # 乗せられる場所があれば、一番大きなものの上に乗せる
        else:
            piles[min_pos] = w

    # 山の数を出力
    print(len(piles))

main()
