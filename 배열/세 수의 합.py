from codingTest import CheckTime


@CheckTime.CheckTime
# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력
def solution1(nums: list) -> list:
    # 브루트 포스 계산
    answer = []
    # 중복값 처리를 위해 정렬
    nums.sort()

    # 브루트 포스 n^3 반복
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        # 이전 값과 현재 값이 같다면, 중복된 결과이므로 연산X
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    answer.append([nums[i], nums[j], nums[k]])
    return answer


@CheckTime.CheckTime
def solution2(nums: list) -> list:
    # 투 포인터 계산
    answer = []
    # 투 포인터 사용을 위해 정렬
    nums.sort()

    for i in range(len(nums) - 1):
        # 중복값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 간격을 좁혀가며 sum 계산
        left = i + 1
        right = len(nums) - 1

        while left < right:
            sum_data = nums[i] + nums[left] + nums[right]
            if sum_data < 0:
                left += 1
            elif sum_data > 0:
                right -= 1
            else:
                # sum 이 0인경우 정답 처리.
                answer.append([nums[i], nums[left], nums[right]])
                # 정답 처리 이후 중복값 건너 뛰고
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # left, right를 한칸씩 이동 후 탐색 재개
                left += 1
                right -= 1
    return answer


solution1([-1, 0, 1, 2, -1, -4])
solution2([-1, 0, 1, 2, -1, -4])
