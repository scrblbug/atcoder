# AtCoder Beginner Contest 198 D - Send More Money
# https://atcoder.jp/contests/abc198/tasks/abc198_d
# tag: 辞書

# 全体的に、Pythonでは時間制限との戦いになる問題。

# 文字と数字の組み合わせ、最大 10! = 3628800 通りを全探索する。
# 組み合わせの生成については、itertools.permutations を使うと便利。

# ……のだが、Pythonでは少しでも効率が悪いと定数倍の影響で間に合わない。
# 下記のコードは最終的なもので、割と素直な全探索の形で実装している。

# 当初書いていたコードでは、辞書変換の後 int(''.join(chars)) の形で
# 文字列 → 数値 への変換を行っていたが、そのままでは間に合わなかった。
# そのコードでも、例えば一桁目だけでも先に確認するようにするなどすれば、
# もう少し速くなって間に合う。

from itertools import permutations
def main():
    s1 = input()
    s2 = input()
    s3 = input()

    # まず重複を取り除き、使われている文字のリストを作成する
    chars = list(set(s1+s2+s3))

    # 文字数が多すぎたら条件3に違反するのでNG
    if len(chars) > 10:
        print('UNSOLVABLE')
        return

    # 例えば len(chars)=3 の時、permutations は
    # (0, 1, 2), (2, 3, 0), (1, 5, 8)... などなど
    # 0 ～ 9 の数字から 3つ取り出した全ての順列を返してくれる。
    for comb in permutations(range(10), len(chars)):
        # ので、その順列毎に辞書を生成してやることで、
        # すべての数字と文字の組み合わせを試行できる
        c_to_n = {k:v for k, v in zip(chars, comb)}

        # 最上位の桁が 0 ならスキップする
        if c_to_n[s1[0]] == 0 or c_to_n[s2[0]] == 0 or c_to_n[s3[0]] == 0:
            continue

        # 文字列 → 辞書変換 → 数値
        # ここを int(''.join(c_to_n[c] for c in s1)) とかやると
        # 間に合わなくなる
        n1 = 0
        for c in s1:
            n1 *= 10
            n1 += c_to_n[c]
        
        n2 = 0
        for c in s2:
            n2 *= 10
            n2 += c_to_n[c]
        
        n3 = 0
        for c in s3:
            n3 *= 10
            n3 += c_to_n[c]
        
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    
    print('UNSOLVABLE')

main()
