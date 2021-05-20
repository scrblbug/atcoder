# 三井住友信託銀行プログラミングコンテスト2019 D - Lucky PIN
# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
# tag: 貪欲法 部分列 高橋君

# 暗証番号は全部で1000種類なので、頑張って
# それぞれが設定可能かどうか全探索してみる。
# O(10^3 * N) なので、間に合うはず……？

# ちなみに、Pythonだと1200ms程度、
# PyPyなら260ms程度なので余裕で間に合う

def main():
    N = int(input())
    S = input()

    result = 0

    for i in range(1000):
        # 面倒くさいのでフォーマットリテラルで 0埋めした文字列で……
        sec_num = [c for c in f'{i:03}']

        # 暗証番号の桁順に、一致したら進めていく貪欲法
        tmp = 0
        for c in S:
            if c == sec_num[tmp]:
                tmp += 1
                if tmp == 3:
                    result += 1
                    break
    print(result)

main()

