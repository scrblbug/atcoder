# AtCoder Indeedなう（予選B） D - 高橋くんと数列
# https://atcoder.jp/contests/indeednow-qualb
# tag: 順列組み合わせ

# 条件を満たす数列の数を求めるのは面倒くさそうなので、
# 条件を満たさないものを撥ねることを考える。
# 対照の数字を a とすると、ある a ~ 次の a 間の数によって、
# 条件を満たさない数列の数を順次求めることが出来る。
# 最後に、それを全ての組み合わせの数から引けば答えが出る

def main():
    N, C = map(int, input().split())
    A = list(map(int, input().split()))

    # 各数字毎に、最後に現れた場所、
    # これまで撥ねた組み合わせの数を管理する辞書を作成
    info_dict = {i:[-1, 0] for i in range(C+1)}

    for i, n in enumerate(A):
        prev, exc = info_dict[n]

        # 間に x 個の別の数字が挟まっているとすると、
        # x * (x+1) / 2 通りの l, r の組を除外できる。
        # [l, r) （ただし l!=r）の開放区間の組み合わせと
        # 考えると分かりやすい
        t = i - prev
        info_dict[n] = [i, exc + t * (t-1) // 2]
    
    # 数列を最後まで見たら、終端の処理を行いつつ
    # 答えを出力する
    all_comb = N * (N+1) // 2

    for i in range(1, C+1):
        prev, exc = info_dict[i]
        t = N - prev
        exc += t * (t-1) //2
        print(all_comb - exc)

main()
