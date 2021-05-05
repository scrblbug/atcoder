# diverta 2019 Programming Contest C - AB Substrings
# https://atcoder.jp/contests/diverta2019/tasks/diverta2019_c
# tag: 考察 文字列 連結 コーナーケース

# 各文字列内に含まれる "AB" はともかくとして。
# それ以外に "AB" が現れるためには、
# "A" で終わる文字列（以下 "*A"）と
# "B" で始まる文字列（以下 "B*"）が必要。
# ただし、"B" で始まり "A" で終わる文字列（以下 "B*A"）も存在するので、
# この 3 種類の文字列をうまく組み合わせる必要がある。

# できるだけ無駄なく A, B を使っていくことを考えると……

# 1. まず "B*A" の文字列を全て連結する
# 2. その端に "*A" と "B*" を連結する
# 3. 他の "*A" と "B*" を組み合わせて連結する
# 4. 改めて全ての文字列を連結する

# という手順を踏めば、無駄なく A, B を使用できる
# ちなみにA, B が無駄になるケースは

# 1. A, B の数が不均等な場合（自明）
# 2. "B*A" を連結したあと、その両端を
#    "*A" もしくは "B*" で "AB" にできない場合

def main():
    N = int(input())
    strings = [input() for _ in range(N)]

    cnt_a = 0
    cnt_b = 0
    cnt_ba = 0
    result = 0

    # "*A", "B*", "B*A" の数をカウント
    # 同時に文字列内の "AB" もカウントしておく
    for s in strings:
        result += s.count('AB')
        if s[0] == 'B' and s[-1] == 'A':
            cnt_ba += 1
        elif s[0] == 'B':
            cnt_b += 1
        elif s[-1] == 'A':
            cnt_a += 1

    # "B*A" が存在する場合
    if cnt_ba > 0:
        # "*A", "B*" がなければ、"B*A" を連結し、その間の数だけ "AB" が増える
        if cnt_a == 0 and cnt_b == 0:
            result += cnt_ba - 1
        # "*A", "B*" どちらかが無ければ、 "B*A" を連結した数だけ "AB" が増える
        elif cnt_a == 0 or cnt_b == 0:
            result += cnt_ba
        # どちらもあるなら、"B*A" を連結し、両端をカバーしたあと
        # 余った "*A", "B*" で "AB" を作成できる
        else:
            result += cnt_ba + 1 + min(cnt_a - 1, cnt_b - 1)
    # "B*A" が存在しない場合
    else:
        result += min(cnt_a, cnt_b)

    print(result)

main()
