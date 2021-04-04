# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import time

user_input = int(input())
start_time = list()
end_time = list()
for _ in range(user_input):
    time_input = input()
    time_input = time_input.split("~")
    start_time.append(time.strptime(time_input[0].strip(), "%H:%M"))
    end_time.append(time.strptime(time_input[1].strip(), "%H:%M"))
max_time = max(start_time)
min_time = min(end_time)
if max_time > min_time:
    print(-1)
else:
    print("{0:02d}:{1:02d} ~ {2:02d}:{3:02d}".format(max_time.tm_hour, max_time.tm_min, min_time.tm_hour, min_time.tm_min))
