# AtCoder Beginner Contest 005
# https://atcoder.jp/contests/abc005/tasks/abc005_3
# tag: 高橋君

# 制約も緩いので、素直に書かれている通りのことを
# 実装していくだけ。
# ここではインデックスを進める形で解いているが、
# キューなどを使用すると多少やりやすいかも？
def main():
    T = int(input())
    N = int(input())
    takoyakis = list(map(int, input().split()))
    M = int(input())
    customers = list(map(int, input().split()))

    # たこ焼き用インデックス
    tkyk_idx = 0

    # 客ごとに見ていく
    for c in customers:
        # たこ焼きが尽きたらNG
        if tkyk_idx >= len(takoyakis):
            print('no')
            return
        # 客の来店に間に合うたこ焼きがなければNG
        if takoyakis[tkyk_idx] > c:
            print('no')
            return
        # たこ焼きが古すぎたら、使えるのが出てくるまで廃棄
        while c - takoyakis[tkyk_idx] > T:
            tkyk_idx += 1
            # 客の来店に間に合わないときはNG
            if tkyk_idx >= len(takoyakis):
                print('no')
                return
        # 客にたこ焼きを渡す
        tkyk_idx += 1
    
    # 客を捌き切ったらOK
    print('yes')

main()
