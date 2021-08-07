# メモ化再帰を用いた場合
import sys
sys.setrecursionlimit(10**9)
def main():
    N = int(input())

    # dpt[x]: x 円を引き出すために必要な最小回数
    dpt = [-1] * (N+1)
    dpt[0] = 0

    def get_min_op(x):
        # メモがあればそれを返す。
        if dpt[x] != -1:
            return dpt[x]
        
        # 最大は x 回
        result = x

        # 1 円を引き出す場合
        tmp_r = get_min_op(x - 1) + 1
        if result > tmp_r:
            result = tmp_r

        # 9^n 円を引き出す場合
        prev = 9
        while prev <= x:
            tmp_r = get_min_op(x - prev) + 1
            if result > tmp_r:
                result = tmp_r
            prev *= 9

        # 6^n 円を引き出す場合
        prev = 6
        while prev <= x:
            tmp_r = get_min_op(x - prev) + 1
            if result > tmp_r:
                result = tmp_r
            prev *= 6
        
        dpt[x] = result
        return result

    result = get_min_op(N)
    print(result)
main()
