# AtCoder Regular Contest 010 B - 超大型連休
# https://atcoder.jp/contests/arc010/tasks/arc010_2
# tag: 日付処理 高橋君 AtCoder国

# datetimeライブラリを使用してもいいが、ここでは年初を 0、
# 年末を 365 にする方針で行っている。
# 振替休日の実装に注意すること。

def main():
    N = int(input())
    holiday_dat = [input() for _ in range(N)]

    # 各月初が何日目かを求めておく
    days_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    csum_days = [0]
    for d in days_of_month:
        csum_days.append(csum_days[-1] + d)

    # 祝日を数値に変換しつつ取り出しておく
    holidays = []
    for s in holiday_dat:
        mth, dy = map(int, s.split('/'))
        holidays.append(csum_days[mth-1] + dy - 1)

        # 後ろから取り出していく予定なので、
        # 降順にソート
        holidays.sort(reverse=True)


    # 土日かどうかを確認する関数
    def weekendp(day):
        return day % 7 == 0 or day % 7 == 6
    
    result = 0  # 回答（最大の連休日数）
    seq = 0     # 現在の連休日数
    stack = 0   # 消化予定の休日数

    for d in range(366):
        # 土日 or 祝日なら消化予定の休日数に加える
        if weekendp(d):
            stack += 1
        
        # 一番はやい祝日と比較し、一致すれば祝日。
        # リストからは pop しておく。
        if len(holidays) > 0 and d == holidays[-1]:
            holidays.pop()
            stack += 1

        # 消化予定の休日があれば、消化する
        if stack > 0:
            stack -= 1
            seq += 1
            if seq > result:
                result = seq
        # 消化予定の休日がなくなれば、連休は途切れる
        else:
            seq = 0

    print(result)

main()

