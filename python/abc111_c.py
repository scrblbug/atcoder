# AtCoder Beginner Contest 111 C - /\/\/\/
# https://atcoder.jp/contests/abc111/tasks/arc103_a
# tag: 数列 考察 コーナーケース

# 奇数番目、及び偶数番目のみで構成される数列を考える。
# この二つの数列が、それぞれ同じ数字に統一されればいい。

# 雑に考えるなら、奇数番目と偶数番目の数列を作成し、
# それぞれ出ている数字をカウントし、一番多く出ている数字に、
# それぞれの数列を統一させる、ということになる。

# ……のだが、それぞれの最頻値が同じ数字になってしまうと
# 条件を満たせない。その場合は、どちらかは 2 番目に
# 多く現れる数字に合わせる必要がある。

# ……のだが、さらにコーナーケースとしては、どちらか（あるいは両方）
# の数列が、一種類しか数字を持っていないというのもある。

# 以上をふまえて……

from collections import Counter
def main():
    n = int(input())
    v = list(map(int, input().split()))

    v_even = v[0::2]
    v_odd = v[1::2]

    # 後でソートするので、カウンターをリストに変換しておく
    cnt_even = [(k, v) for k, v in Counter(v_even).items()]
    cnt_odd = [(k, v) for k, v in Counter(v_odd).items()]

    # 一種類しかない例外を除くため、「0 個の数字」を追加しておき、
    # 個数の降順にソートしておく
    cnt_even.append((0, 0))
    cnt_odd.append((0, 0))
    cnt_even.sort(key=lambda x:x[1], reverse=True)
    cnt_odd.sort(key=lambda x:x[1], reverse=True)

    # 別々の最頻値を持っていれば、それに合わせる
    if cnt_even[0][0] != cnt_odd[0][0]:
        result = n - cnt_even[0][1] - cnt_odd[0][1]
    
    # 最頻値が同じなら、次に多く出ている数字をそれぞれ試し、
    # よい値の方を取るようにする
    else:
        result = n - max(cnt_even[0][1] + cnt_odd[1][1], cnt_even[1][1] + cnt_odd[0][1])
    
    print(result)

main()
