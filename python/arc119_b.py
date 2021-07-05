# AtCoder Regular Contest 119 B - Electric Board
# https://atcoder.jp/contests/arc119/tasks/arc119_b
# tag: 考察 数列 入れ替え 一致

# 01111 <-> 11110

# 入力例1で考える。
# 1110110
# 1011110 : 真ん中の 0 を左へ移動
# 1010111 : 右端の 0 を左へ移動
# のように、0 を左右に移動させると捉えると理解しやすい。
# 1 は空いているスペースに相当する。

# となると、元の数列の n 番目の 0 を、最後の数列の n 番目に
# 移動させると考えればいい。

# 1) すでに一致していれば移動させなくていい。
# 2) 移動先までの間に他の 0 がなければ一手で移動させる。
# 3) 移動先までの間に他の 0 があれば、それを先に一致させる。

# という手順を踏むことで、
# (0 の個数) - (元々場所が一致している 0 の個数)
# の手数で完了できる。（常に 0 が足りなくなっている端から
# 一致させるような動きになる）

def main():
    N = int(input())
    S = [int(c) for c in input()]
    T = [int(c) for c in input()]


    # それぞれの 0 の場所を確認
    s_pos = []
    for i in range(N):
        if S[i] == 0:
            s_pos.append(i)
    t_pos = []
    for i in range(N):
        if T[i] == 0:
            t_pos.append(i)
    
    # 0 の個数が一致していなければ不可能
    if len(s_pos) != len(t_pos):
        print(-1)
        return

    result = len(s_pos)

    # 元々移動させる必要がない 0 の個数分を引く
    for i in range(len(s_pos)):
        if s_pos[i] == t_pos[i]:
            result -= 1
    
    print(result)

main()
