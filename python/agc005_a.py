# AtCoder Grand Contest 005 A - STring
# https://atcoder.jp/contests/agc005/tasks/agc005_a
# tag: 文字列 削除 文字数 愚直 スタック 高橋君

# 公式解説ではスタックを用いた愚直解に近いものになっている。
# 早いし書きやすい。

def main():
    S = input()

    # スタック初期化。一応関係ない文字を入れておく。
    st = ['X']

    # 与えられた文字列を順番に処理
    for c in S:
        # S ならそのままスタック行き
        if c == 'S':
            st.append(c)
        
        # T かつ スタックの最後が S なら、
        # スタックの最後の削除のみ （ST を消す作業）
        elif st[-1] == 'S':
            st.pop()
        
        # T かつスタックの最後が T ならスタック行き
        else:
            st.append(c)

    # 初期化用の文字を差し引いて回答
    print(len(st)-1)

main()

# 以下、僕が最初に思いついた回答。
# 操作により、T より左側にある S は全て無くなってしまう。
# つまり、最後はTTTTSSSS のような形になる。

# S の後に T が来た場合、その T は無くなる……といった
# 考え方をして、とりあえず左端から順に T なら +1, S なら -1
# していくことにすると……

# 入力例 3 の場合
# T  S  S  T  T  T  S  S
# 1  0 -1  0  1  2  1  0

# のように、出来上がった数列の最大値が、左端に残る T の
# 個数ということになる（ただし、最小値はもちろん 0 ）。

# 問題文の条件より、元々 S と T は同じ数あるはずなので、
# 当然残る数も同じ。

def main2():
    S = input()
    cnt = []
    tmp = 0
    for c in S:
        if c == 'T':
            tmp += 1
        else:
            tmp -= 1
        cnt.append(tmp)

    # 左に残る T の数
    left = max(0, max(cnt))

    print(left * 2)

# main2()
