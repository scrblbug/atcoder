# AtCoder Regular Contest 009 B - おとぎの国の高橋君
# https://atcoder.jp/contests/arc009/tasks/arc009_2
# tag: 辞書 高橋君

# AtCoder国と普通の数字の（文字列での）変換辞書を作成し、
# AtCoder数を文字列で受け取り、普通の数字へと変換後、
# ソートを行う

def main():
    atcoder_n = [c for c in input().split()]
    N = int(input())
    atcoder_nums = [input() for _ in range(N)]

    # 辞書作成
    a_to_n = {k:str(v) for v, k in enumerate(atcoder_n)}

    # 受け取ったAtCoder数字文字列 → 普通の数字文字列 → 数値と
    # 変換した後、インデックス付きで保存していく
    num_with_index = []
    for i, a_num in enumerate(atcoder_nums):
        n = int(''.join(a_to_n[c] for c in a_num))
        num_with_index.append((n, i))

    # ソート後、インデックスを元にしてAtCoder数で出力
    num_with_index.sort()
    for item in num_with_index:
        print(atcoder_nums[item[1]])

main()
