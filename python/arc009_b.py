# AtCoder Regular Contest 009 B - おとぎの国の高橋君
# tag: 辞書 基礎問題 高橋君

# AtCoder国と普通の数字の（文字列での）変換辞書を作成し、
# AtCoder数を文字列で受け取り、普通の数字へと変換後、
# ソートを行う

def main():
    atcoder_n = [c for c in input().split()]
    N = int(input())
    numbers = [input() for _ in range(N)]

    # 辞書作成
    a_to_n = {k:str(v) for v, k in enumerate(atcoder_n)}

    # 受け取ったAtCoder数字文字列 → 普通の数字文字列 → 数値と
    # 変換した後、インデックス付きで保存していく
    n_with_index = []
    for i, atcoder_number in enumerate(numbers):
        n = int(''.join(a_to_n[c] for c in atcoder_number))
        n_with_index.append((n, i))

    # ソート後、インデックスを元にしてAtCoder数で出力
    n_with_index.sort()
    for item in n_with_index:
        print(numbers[item[1]])

main()
