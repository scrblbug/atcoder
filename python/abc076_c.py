# AtCoder Beginner Contest 076 C - Dubious Document 2
# https://atcoder.jp/contests/abc076/tasks/abc076_c
# tag: 文字列 辞書順 正規表現

# 自明なこととして、辞書順最小を目指すので、? は可能な限り a に
# 変えるほうがいい。

# しかし、T と一致する部分が最低一箇所は必要。
# 一致箇所が複数ある場合を考える。
# 便宜的に左と右で考えてみると、左側で一致させる場合よりも、
# 右側で一致させるほうが、より左側の ? を a に変更することが
# できる。よって、可能な限り右側で一致させるほうがいい。

# ちなみに公式解説では置き換え可能な全てを求め、
# その中で辞書順最小を出力、としている。
# 制約も緩いので、どちらでもいいかと思う。

def main():
    S = input()
    T = input()

    # T との置換を始める地点を result とする
    result = -1

    # S 上の、|S| - |T| の地点から左に向かって、そこから右の文字列が
    # T と一致 or 置換可能かどうかを探索していく。
    # '(c|?)(o|?)(d|?)...' という感じで組み立てて、正規表現で
    # やってしまう手もあるかもしれないが、やや煩雑かも。
    for start in range(len(S) - len(T), -1, -1):
        for i in range(len(T)):
            # 一文字ずつ一致 or 置換可能かどうかを確認
            if S[start + i] == T[i] or S[start + i] == '?':
                continue
            # 不一致ならスタート地点を左へずらす
            else:
                break

        # 全文字が一致 or 置換可能なら、result を出して break
        else:
            result = start
            break
    
    # result が -1 のままなら、T への置換が不可能
    if result == -1:
        print('UNRESTORABLE')

    # result に値があれば、そこからを T へ置き換え、
    # 他の ? は a に置換して出力
    else:
        S = S.replace('?', 'a')
        print(S[:result] + T + S[result+len(T):])

main()
