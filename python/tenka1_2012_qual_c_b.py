# 天下一プログラマーコンテスト2012 予選C B - ロイヤルストレートフラッシュ
# https://atcoder.jp/contests/tenka1-2012-qualC/tasks/tenka1_2012_10
# tag: 文字列 正規表現

# カード情報が 2文字のものと 3文字のものが混在しているので、
# まずはそこを統一してから始めるとやりやすい。

# また、同じカードが 2枚以上無いことを踏まえると、
# とりあえず（仮にスペードとすると） 'S1' ～ 'S9' 以外のものが
# 5 枚現れればよい。

def main():
    S = input()
    
    # 10 → T として分かりやすくしておく。
    S = S.replace('10', 'T')

    # スートごとの必要札をカウントしていく。
    appeared = {'S':0, 'H':0, 'D':0, 'C':0}

    for i in range(0, len(S), 2):
        suit = S[i]
        rank = S[i+1]

        if rank not in '123456789':
            # 10 以上ならスート別にカウントしていく。
            appeared[suit] += 1

            # 5枚以上現れた段階で打ち切る。
            if appeared[suit] == 5:
                used = i
                break

    # break した地点と suit を元に、捨札を再構成する。
    used_cards = S[:used+2]

    # 使用するカードを取り除く。
    for r in 'TJQKA':
        used_cards = used_cards.replace(suit+r, '')
    
    # 'T' を戻すのを忘れないように。
    used_cards = used_cards.replace('T', '10')

    if used_cards == '':
        print(0)
    else:
        print(used_cards)

main()

# 正規表現を用いて解くことも可能。
# 制約が緩いので、多少効率が悪くても十分通る。
import re
def main2():
    S = input()

    # スートごとの正規表現のパターンを作っておく
    patterns = [f'{s}10|{s}J|{s}Q|{s}K|{s}A' for s in 'SHDC']

    # 一文字ずつ増やしながらチェックしていく
    for i in range(len(S)):
        checking = S[:i+1]

        # findall でスートごとに対象のカードを抽出
        for p in patterns:
            rs_cards = re.findall(p, checking)

            # 5枚あった段階で、捨札を再構成
            if len(rs_cards) == 5:
                result = checking

                # 使用したカードを取り除く。
                for card in rs_cards:
                    result = result.replace(card, '')

                print(result if len(result) > 0 else 0)
                return
# main2()
