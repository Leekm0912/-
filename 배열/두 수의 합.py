def solution1(nums: list, target: int) -> list:
    # 무차별 대입(브루트 포스)
    for i in range(len(nums)):
        # i보다 한칸 뒤에서부터 찾음
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def solution2(nums: list, target: int) -> list:
    # target - 첫번째값이 있는지 확인.
    for i, n in enumerate(nums):
        complement = target - n
        # i보다 한칸 뒤에서부터 찾음.
        if complement in nums[i + 1:]:
            # 뒤에 숫자를 찾을때는 i+1부터 찾기때문에 인덱스 연산시 i+1을 해줌.
            return [nums.index(n), nums[i + 1:].index(complement) + (i+1)]


def solution3(nums: list, target: int) -> list:
    # map을 이용해 첫번째 수를 뺀 결과 키 조회
    nums_map = {}
    # key: 값, value: index로 저장
    # => 조회시 값으로 인덱스를 찾을 수 있음.
    for i, v in enumerate(nums):
        nums_map[v] = i

    for i, v in enumerate(nums):
        # 첫번째 수가 map에 있고, 첫번째 수와 같은 인덱스가 아니라면 정답.
        if target - v in nums_map and i != nums_map[target - v]:
            return [i, nums_map[target - v]]


def solution4(nums: list, target: int) -> list:
    # 3번에서 조회구조를 개선.
    nums_map = {}
    # 하나의 for문으로 통합.
    for i, v in enumerate(nums):
        # 첫번째 수가 nums_map에 들어있다면.
        if target - v in nums_map:
            # 첫번쨰 수의 인덱스와, 현재 인덱스를 리턴
            return [nums_map[target - v], i]
        # 들어있지 않다면 값:인덱스로 저장.
        nums_map[v] = i


print(solution1([2, 7, 11, 15], 9))
print(solution2([2, 7, 11, 15], 9))
print(solution3([2, 7, 11, 15], 9))
print(solution3([3, 11, 3, 15], 6))
print(solution4([2, 7, 11, 15], 9))
print(solution4([3, 11, 3, 15], 6))