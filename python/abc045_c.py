# AtCoder Beginner Contest 045 C - たくさんの数式
# https://atcoder.jp/contests/abc045/tasks/arc061_a
# tag: bit全探索 典型問題

def main():
    S = input()

    result = 0

    # ある文字の直後に '+' を入れるかどうかで全探索
    for st in range(1<<(len(S)-1)):
        # 現在の数字
        tmp = 0
        for i, c in enumerate(S):
            # 前の数字と繋げる。
            # 直前に '+' があるとき（or 左端）は、tmp = 0 としておく。
            tmp = tmp * 10 + int(c)

            # 次に '+' なら、一旦数字を切る
            if st>>i & 1:
                result += tmp
                tmp = 0

        # 残った分を足す
        result += tmp
    # 回答
    print(result)

main()
