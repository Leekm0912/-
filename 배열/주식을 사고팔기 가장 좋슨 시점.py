import sys
from codingTest import CheckTime


@CheckTime.CheckTime
def solution1(prices: list) -> int:
    max_price = 0
    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)
    return max_price


@CheckTime.CheckTime
def solution2(prices):
    answer = 0
    min_price = sys.maxsize
    for price in prices:
        min_price = min(price, min_price)
        answer = max(price - min_price, answer)
    return answer


solution1([7, 1, 5, 3, 6, 4])
solution2([7, 1, 5, 3, 6, 4])
