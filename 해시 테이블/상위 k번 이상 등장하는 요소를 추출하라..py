import collections

from CheckTime import CheckTime


@CheckTime
def solution1(nums, k):
    table = {}
    for i in nums:
        if i not in table:
            table[i] = 1
        else:
            table[i] += 1

    result = []
    for key in table:
        if table[key] >= k:
            result.append(key)
    return result


if __name__ == "__main__":
    print(solution1(nums=[1, 1, 1, 2, 2, 3], k=2))
