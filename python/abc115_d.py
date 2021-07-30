# AtCoder Beginner Contest 115 D - Christmas
# https://atcoder.jp/contests/abc115/tasks/abc115_d
# tag: 再帰関数 高羽氏 ルンルン

# 再帰構造を持っているので、そのまま
# 書き起こすと書きやすいかもしれない。
# 5層構造なので、そこをきちんとサボらずに書いていくと
# バグらせにくい。

def main():
    N, X = map(int, input().split())

    # とりあえず各レベルのバーガーが
    # 何層構造なのかを求めておく。
    whole = [1]
    for lv in range(1, 51):
        whole.append(3 + 2 * whole[-1])

    memo = dict()

    # レベル lv のバーガーを下から x 枚食べた
    # 時のパティの枚数を求める
    def get_putty_num(lv, x):
        # lv0 なら、パティ1枚のみ
        # x==0 なら 0, x==1 なら 1 を返す
        if lv == 0:
            return x

        # 0 ～ 1 枚なら、パティは 0 枚
        if x <= 1:
            return 0


        # メモを参照する
        if (lv, x) in memo:
            return memo[(lv, x)]

        result = 0

        # 中央より下しか食べてない場合
        if x <= whole[lv] // 2:
            result = get_putty_num(lv-1, x-1)

        # ちょうど中央まで
        elif x == whole[lv] // 2 + 1:
            result = get_putty_num(lv-1, whole[lv-1]) + 1

        # 最後の 1 枚を除くまで
        elif x <= whole[lv] - 1:
            result += get_putty_num(lv-1, whole[lv-1])
            result += 1
            result += get_putty_num(lv-1, x - whole[lv]//2 - 1)

        # 最後の 1 枚まで
        else:
            result = get_putty_num(lv-1, whole[lv-1]) * 2 + 1

        # メモした後、結果を返す
        memo[(lv, x)] = result
        return result

    # 作成した再帰関数を元に回答
    print(get_putty_num(N, X))

main()
