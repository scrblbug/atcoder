# AtCoder Regular Contest 027 B - 大事な数なのでZ回書きまLた。
# https://atcoder.jp/contests/arc027/tasks/arc027_2
# tag: グラフ 連結成分

# s1とs2の同じ箇所に出てくるものは同じ数を表す
# そこで、同じものを表す文字を辺でつなげたグラフを作成し、
# 各連結成分を確認する。
# 連結成分に数字が含まれていれば、それらの文字は確定済み
# 数字が含まれていない場合は、一文字目に使われている文字が
# 含まれている場合、1～9のどれか。それ以外は0～9のどれかとなる。

def main():
    N = int(input())
    s1 = input()
    s2 = input()

    nums = '0123456789'

    # グラフの辺情報として読み込む
    link = dict()
    for a, b in zip(s1, s2):
        if a not in link:
            link[a] = set()
        if b not in link:
            link[b] = set()
        link[a].add(b)
        link[b].add(a)
    
    # 探索済み文字群
    checked = set()

    # 連結成分を格納するリスト
    groups = []

    # 連結成分探索
    for item in link.keys():
        if item in checked:
            continue
        group = set()
        queue = [item]
        while queue:
            now = queue.pop()
            for nxt in link[now]:
                if nxt in group:
                    continue
                group.add(nxt)
                queue.append(nxt)
        checked = checked | group
        groups.append(group)
    
    result = 1

    # 改めて、各連結成分の中身を確認する
    for g in groups:
        # 数字が含まれているか？
        ncount = 0
        for n in nums:
            if n in g:
                ncount += 1
        
        # 複数の数字が含まれる＝矛盾
        if ncount > 1:
            result = 0
            break

        # 数字がひとつ含まれる＝確定群
        if ncount == 1:
            continue

        # 一文字目に使われているもの
        if s1[0] in g or s2[0] in g:
            # 一文字に0が確定する＝矛盾
            if '0' in g:
                result = 0
                break
            # そうでなければ、1～9のどれでも良い
            result *= 9
        else:
            # 一文字目に使われていなければ、0～9のどれでも良い
            result *= 10
    
    print(result)

main()
