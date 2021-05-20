# AtCoder Beginner Contest 113 C - ID
# https://atcoder.jp/contests/abc113/tasks/abc113_c
# tag: 事前ソート AtCoder国

def main():
    N, M = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(M)]

    # 市それぞれに認識番号をつけた後、年順にソートしておく
    for i in range(M):
        cities[i].append(i)
    cities.sort(key=lambda x:x[1])

    # 各県に割り振られた市の数を管理
    id_by_pref = [0] * (N+1)

    # 市（認識番号）ごとのIDを保存していくリスト
    id_list = [""] * M

    # 年順にソート済みなので、順番に県に割り振っていけばよい
    for city in cities:
        pref, year, idx = city

        # 該当県の割り振り数を加算し、IDを作成・保存する
        id_by_pref[pref] += 1
        id = f'{pref:06}{id_by_pref[pref]:06}'
        id_list[idx] = id
    
    # 改めて認識番号順に出力
    for i in range(M):
        print(id_list[i])

main()
