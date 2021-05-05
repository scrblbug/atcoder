# AtCoder Grand Contest 016 A - Shrinking
# https://atcoder.jp/contests/agc016/tasks/agc016_a
# tag: 考察

# ある単一の文字 c にまとめることを考える。
# c と c の間に文字が入っている時、
# c ? ? ? c → c ? ? c → c ? c というように、
# 間は一文字ずつ縮まっていく。ちなみに文字列の端も同様で、
# ? ? c → ? c → c となっていく。
# したがって、c と c の間が一番広い部分をみつけ、
# そこと同じ回数だけ操作を行う必要がある。

def main():
    s = input()
    # 使われている文字のセットを作る
    ch_set = set(c for c in s)

    result = len(s)
    # どの文字に統一するかは全探索する
    for c in ch_set:
        # splitを用いて分割し、一番長い部分の長さを求める
        tmp_r = max(len(p) for p in s.split(c))

        if tmp_r < result:
            result = tmp_r

    print(result)

main()
