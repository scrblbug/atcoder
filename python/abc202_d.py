# AtCoder Beginner Contest 202 D - aab aba baa
# https://atcoder.jp/contests/abc202/tasks/abc202_d
# tag: 文字列 辞書順 順列・組み合わせ パスカルの三角形

# 上から順番に文字を決定していく。

# まず、'a', 'b' の個数をそれぞれ a, b とする。
# このとき、'a' 'b' の組み合わせによる文字列の総数を
# 考えると、(a + b) 箇所から a 個の 'a' になる場所を
# 選ぶことになるので、a+b C a 通りとなる。

# ここで、最初の文字を仮定してみる。

# 最初の文字が 'a':
# 'a' + (a-1個の'a' と b個の'b'による文字列)
# これは、a+b-1 C a-1 種類

# つまり、a+b-1 C a-1 番目より後なら、
# 最初の文字は 'b' ということになる。

# 以下、最初の文字が 'a' ならそのまま繰り返す。
# 'b' なら、'b'の中での順位を考慮する必要があるので、
# 辞書順から前回の判定で使った組み合わせ数を引いて繰り返す。


def main():
    a, b, k = map(int, input().split())

    # まずは n C r を素早く求められるようにしておくが、
    # ここではパスカルの三角形を用いてみた。
    # これにより、二種類のものがそれぞれ a, b 個あるときに、
    # その順列の組み合わせ数を comb[a][b] で求められる。
    comb = [[0] * 61 for _ in range(61)]
    comb[0][0] = 1

    for i in range(61):
        for j in range(61):
            if i > 0:
                comb[i][j] += comb[i-1][j]
            if j > 0:
                comb[i][j] += comb[i][j-1]

    # 文字列をその都度合成していくと、度に新たな文字列を生成する
    # ＝文字列の長さ分の計算量が掛かるため、配列に保存しておき、
    # 後から合成するほうが良い。
    result = []

    while True:
        # 順位と、最初が 'a' になる通り数を比較する。
        # 最初が 'a' になる場合
        if k <= comb[a-1][b]:
            result.append('a')
            a -= 1
        # 最初が 'b' になる場合
        else:
            result.append('b')
            k -= comb[a-1][b]
            b -= 1
        # a, b どちらかが 0 になれば残りが確定するので終了
        if a == 0 or b == 0:
            break
    
    # 余っている 'a' / 'b' を後ろにくっつけて回答
    print(''.join(result) + 'a'*a + 'b'*b)

main()
