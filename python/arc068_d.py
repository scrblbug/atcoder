# AtCoder Regular Contest 068 D - Card Eater
# https://atcoder.jp/contests/arc068/tasks/arc068_b
# tag: 考察 ゲーム 一人ゲーム すぬけ君

# 3枚以上ある同一のカードについては、
# 同じカードを 3枚選ぶことで 2枚減らすことが出来る。
# この操作により、1枚 or 2枚残る状態まではカードを破棄可能。

# そこで、最終的に 2枚残っているカードについて考える。
# このカードのうち、AAB のような形で選ぶことで、2 種類の
# カードから 1枚ずつ破棄することが出来る。

# よって、最大効率でカードを破棄していった場合、
# 毎回 2枚ずつ捨てていくという制限によってのみ
# 最後に残せるカードの種類数は決定される。

def main():
    N = int(input())
    A = list(map(int, input().split()))

    result = len(set(A))

    # 種類数が偶数なら、全て残すのは不可能
    if result % 2 == 0:
        result -= 1

    print(result)

main()
