# datetime を用いた実装。
from datetime import date, timedelta

# start ～ end の date を返し続けるジェネレータ
def date_range(start, end, step=timedelta(1)):
    now = start
    while now < end:
        yield now
        now += step

# 日付を date オブジェクトとして管理することを除けば
# あとは同様に実装していく。
def main():
    N = int(input())
    hd_dat = [input() for _ in range(N)]
    holidays = []
    for hd in hd_dat:
        m, d = map(int, hd.split('/'))
        holidays.append(date(2012, m, d))

    holidays.sort(reverse=True)

    result = 0
    stock = 0
    seq = 0
    for td in date_range(date(2012,1,1), date(2013,1,1)):
        if td.weekday() == 6 or td.weekday() == 5:
            stock += 1
        if len(holidays) > 0 and td == holidays[-1]:
            stock += 1
            holidays.pop()

        if stock > 0:
            stock -= 1
            seq += 1
            if seq > result:
                result = seq
        else:
            seq = 0

    print(result)

main()