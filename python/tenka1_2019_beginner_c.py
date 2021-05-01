# Tenka1 Programmer Beginner Contest 2019 C - Stones
# https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_c
# tag: 考察

# 最終的には、全ての白い石が黒い石より左側になければならない。
# つまり、必ず
# .....########
# のように、左から n 個白い石が続いた後、m 個黒い石が続くような
# ものになる(n >= 0, m >= 0)。

# 問題は白い石がいくつ目まで続いた後黒い石に切り替わるかということに
# なるので、それを全探索する。

# n 個目まで白い石とすると、n 個目までに含まれる黒い石と、
# n+1 個目以降に含まれる白い石を変更する必要がある。
# n を左側から見ていくとした場合、黒い石については
# 出てきた時に数えればいい。
# 白い石については、あらかじめ全体の個数を数えておき、
# 出てきた分を引けばいい。

def main():
    N = int(input())
    S = input()

    # 白の数を数えておく
    n_white = S.count('.')
    
    # 石を全部黒にするケースからスタート
    result = n_white

    # 石をひとつずつ進めていく
    n_black = 0
    for c in S:
        if c == '.':
            n_white -= 1
        elif c == '#':
            n_black += 1
        result = min(result, n_white + n_black)

    print(result)

main()
