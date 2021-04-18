import datetime
def solution(a, b):
    day = ["MON","TUE","WED","THU","FRI","SAT","SUN"];
    return day[datetime.datetime(2016, a, b).weekday()];