import collections

from codingTest import CheckTime


@CheckTime.CheckTime
def solution1(J, S):
    table = {}

    for c in S:
        if c not in table:
            table[c] = 1
        else:
            table[c] += 1

    result = 0
    for c in J:
        if c in table:
            result += table[c]
    return result


@CheckTime.CheckTime
def solution2(J, S):
    table = collections.defaultdict(int)
    for c in S:
        if c in J:
            table[c] += 1
    return sum(table.values())


@CheckTime.CheckTime
def solution3(J, S):
    table = collections.Counter(S)
    result = 0
    for c in J:
        result += table[c]
    return result


@CheckTime.CheckTime
def solution4(J, S):
    return sum(s in J for s in S)


if __name__ == "__main__":
    print(solution1(J="aA", S="aAAbbbb"))
    print(solution2(J="aA", S="aAAbbbb"))
    print(solution3(J="aA", S="aAAbbbb"))
    print(solution4(J="aA", S="aAAbbbb"))
