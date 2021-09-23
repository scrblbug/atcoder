# AtCoder Grand Contest 048 A - atcoder < S
# https://atcoder.jp/contests/agc048/tasks/agc048_a
# tag: 文字列 辞書順 隣接操作 すぬけ君

# そもそも S > atcoder なら、0。

# それ以外の場合、 a 以外の文字があれば、
# その文字を最初に持ってくることで atcoder < S と出来る。

# そのため、一番左側にある a 以外の文字を、一番左まで
# 持ってくるのが最短……なのだが、手前が t なので、t より
# 大きい文字なら、左から二番目まででいい。

# ……という、上記の説明で微妙な気持ちになった場合、
# b, ab, aab, at, aat, az, aaz などの各場合について考慮すれば、
# 上記の仮定が正しいことが分かる。

def main():
    T = int(input())
    queries = [input() for _ in range(T)]

    for S in queries:
        # 元々条件を満たしていれば、0 を返す。
        if S > 'atcoder':
            print(0)
            continue

        for i, c in enumerate(S):
            if c == 'a':
                continue
            
            # t より小さい文字なら左端まで動かす。
            if c <= 't':
                print(i)
                break

            # t より大きい文字なら動かすのは二番目まででいい。
            # ただし元々左端なら 0 を返す。
            else:
                print(max(0, i-1))
                break
        # a 以外の文字が見つからなければ、-1 を返す。
        else:
            print(-1)

main()
