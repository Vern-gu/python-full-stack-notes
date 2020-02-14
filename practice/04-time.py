import datetime,time


def get_age():
    """计算年龄"""
    year, month, day = input("input birthday e.g.2018/10/10\n").split("/")
    birthday = datetime.datetime(int(year), int(month), int(day))
    now = datetime.datetime.now()
    now.strftime("%Y/%m/%d")
    ages = (now-birthday).days//365
    print(ages)


def alarm(h, m):
    """闹钟计时"""
    while 1:
        current_time = time.localtime()[3:6]
        print("%02d:%02d:%02d"% current_time, end="\r")
        if current_time[0:2] == (h,m):
            print("time up")
            break
        time.sleep(1)


if __name__ == '__main__':
    get_age()
    alarm(22,6)



