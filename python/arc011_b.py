# AtCoder Regular Contest 011 B - ルイス・キャロルの記憶術
# https://atcoder.jp/contests/arc011/tasks/arc011_2
# tag: 辞書 コーナーケース

# 一種の暗号解読問題。
# 解き方というのは特に無いので粛々と実装していく。

def main():
    N = int(input())
    words = list(input().split())

    # 変換辞書の作成
    # それこそ一発書きでもなんでも、やりやすいやり方でいいと思うが、
    # なるべく間違えにくいように、生成する形を取っている。
    letters = ['bc', 'dw', 'tj', 'fq', 'lv', 'sx', 'pm', 'hk', 'ng', 'zr']
    c_to_n = dict()
    for l, n in zip(letters, '1234567890'):
        for c in l:
            c_to_n[c] = n

    result = []
    for w in words:
        tmp = []
        for c in w:
            # 大文字小文字を区別しないよう、lower() を使用
            if c.lower() in c_to_n:
                # tmp を文字列として、tmp = tmp + c_to_n[c.lower()]
                # としても良いが、いちいち新規の文字列が作成されるため、
                # 遅くなる。後から ''.join() してやる方が速い。
                # ……もっとも、この問題の制約では大した意味はない。
                tmp.append(c_to_n[c.lower()])

        # tmp の中身があるときだけ答えに追加
        if tmp:
            result.append(''.join(tmp))

    print(*result)

main()