from codingTest import  CheckTime


@CheckTime.CheckTime
def solution(scores):
    answer = ''
    # 리스트를 자기 자신의 성적만 오도록 뒤집음.
    new_scores = list(map(list, zip(*scores)))

    for index, student in enumerate(new_scores):
        score = 0
        # 자기 자신이 평가한 점수가 최고 또는 최저점이라면 삭제.
        if max(student) == student[index] or min(student) == student[index]:
            # 자기 자신과 동일한 점수를 준 사람이 있다면 제외.
            if student.count(student[index]) == 1:
                student.remove(student[index])
        # 스코어 계산.
        score = sum(student) / len(student)
        if score >= 90:
            answer += "A"
        elif score >= 80:
            answer += "B"
        elif score >= 70:
            answer += "C"
        elif score >= 50:
            answer += "D"
        else:
            answer += "F"
    return answer


if __name__ == "__main__":
    solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65],
              [24, 90, 94, 75, 65]])
    solution([[50, 90], [50, 87]])
    solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]])
