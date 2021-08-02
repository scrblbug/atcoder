# CADDi 2018 D - Harlequin
# https://atcoder.jp/contests/caddi2018/tasks/caddi2018_b
# tag: ゲーム 二人ゲーム 考察 ルンルン

# 相手の手番の時に、各色のりんごの数が、全て偶数だとする。
# すると、相手が食べたりんごを、自分も同じ組み合わせで
# 食べることで「各色のりんごの数が全て偶数である状態」を
# 維持できる。
# この行動を続けることで、いずれ自分の手番で
# 「りんごの数を全て 0」にすることができる。

# つまり、最初の状態でりんごの個数が全て偶数なら、負け。
# 違っていれば、奇数のものだけ食べて開始すれば勝ちになる。

def main():
    N = int(input())
    apples = [int(input()) for _ in range(N)]

    # 全て偶数かどうかチェックし、回答
    if all(v % 2 == 0 for v in apples):
        print('second')
    else:
        print('first')

main()
