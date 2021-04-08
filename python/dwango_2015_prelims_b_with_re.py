# dwangoプログラミングコンテスト B - ニコニコ文字列
# https://atcoder.jp/contests/dwango2015-prelims/tasks/dwango2015_prelims_2
# tag: 文字列 正規表現 考察

# せっかくなので、いろいろと試してみる

# replaceを使って処理してやると、簡単になる
def main():
    S = input()

    # 入力例2 の場合、
    # "1251251252525" → "1X1X1XXX" → " X X XXX"
    # → ["X", "X", "XXX"] としてやるイメージ
    S = S.replace('25', 'X')
    for i in range(10):
        S = S.replace(str(i), ' ')
    result = 0
    for s in S.split():
        result += (len(s) + 1) * len(s) // 2
    print(result)
main()

# 正規表現を用いてもいい
import re
def main2():
    S = input()
    S = re.sub(r'25', 'X', S)
    S = re.sub(r'\d+', ' ', S)
    print(sum((len(s)+1)*len(s)//2 for s in S.split()))
# main2()

# finditer, findallを用いる手もある
import re
def main3():
    S = input()
    match = re.finditer(r'(25)+', S)
    result = 0
    for g in match:
        # group() はグルーピングした部分だけでなく、マッチ全体を返す
        n = len(g.group()) // 2
        result += (n + 1) * n // 2
    
    print(result)
# main3()

import re
def main4():
    S = input()
    # findall の場合、25の繰り返し部を後から拾う必要がある
    match = re.findall(r'((?:25)+)', S)
    result = 0
    for g in match:
        n = len(g) // 2
        result += (n + 1) * n // 2
    
    print(result)
# main4()
