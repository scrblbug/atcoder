# CODE FESTIVAL 2017 qual A B- fLIP
# https://atcoder.jp/contests/code-festival-2017-quala/tasks/code_festival_2017_quala_b
# tag: グリッド 考察

# 各行・列のボタンに関しては、自由に入れ替え可能。
# よって、最終的に問題になるのは、それぞれいくつずつ
# 反転されているかということ。

# p 行分と q 列分のが反転している時、黒になっているマスの数を考えると、
# (M-q) * p + (N-p) * q となる。（図を書くと分かりやすい）

# というわけで、書く場合については O(1) で求めることができ、
# 制限が 1 <= N <= 1000, 1 <= M <= 1000 なので、全探索を行う。

def main():
    N, M, K = map(int, input().split())

    # 上記の式を用いて全探索
    for p in range(N+1):
        for q in range(M+1):
            # 見つかれば 'Yes' にして break
            if (M-q) * p + (N-p) * q == K:
                result = 'Yes'
                break
        else:
            continue
        # 多重ループ脱出用 break
        break
    # 見つからなければ 'No'
    else:
        result= 'No'

    print(result)

main()
