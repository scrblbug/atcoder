# AtCoder Beginner Contest 015 C - 高橋くんのバグ探し
# https://atcoder.jp/contests/abc015/tasks/abc015_3
# tag: 基礎問題 高橋君

# 制約から、回答の組み合わせは高々 5^5 = 3125 通りなので
# 全探索を行う。

def main():
    N, K = map(int, input().split())
    questions = [list(map(int, input().split())) for _ in range(N)]

    # 回答により現れる数値を保存
    patterns = [0]

    # 質問毎に得られる数値のパターンを更新していく
    for q in questions:
        # 更新用の新規リスト
        new_patterns = []

        # 前回の数値と今回の回答をすべて組み合わせ、
        # xor したものを新しいパターンとする
        for p in patterns:
            for choice in q:
                new_patterns.append(p^choice)

        # 更新して次の質問へ
        patterns = new_patterns

    if 0 in patterns:
        print('Found')
    else:
        print('Nothing')

main()

# せっかくなので再帰でも
def main2():
    N, K = map(int, input().split())
    questions = [list(map(int, input().split())) for _ in range(N)]

    def dfs(q_no, now):
        if q_no == N:
            if now == 0:
                return True
            else:
                return False

        for a in questions[q_no]:
            if dfs(q_no+1, now^a):
                return True
        else:
            return False

    if dfs(0, 0):
        print('Found')
    else:
        print('Nothing')

# main2()
