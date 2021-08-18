def solution(numbers, hand):
    answer = ''
    left_now = [3, 0]
    right_now = [3, 2]
    hands_pos = {
        1: (0, 0),
        4: (1, 0),
        7: (2, 0),
        2: (0, 1),
        5: (1, 1),
        8: (2, 1),
        0: (3, 1),
        3: (0, 2),
        6: (1, 2),
        9: (2, 2),
    }

    for n in numbers:
        if n in (2, 5, 8, 0):
            left = abs(left_now[0] - hands_pos[n][0]) + abs(left_now[1] - hands_pos[n][1])
            right = abs(right_now[0] - hands_pos[n][0]) + abs(right_now[1] - hands_pos[n][1])
            if left < right:
                left_now = hands_pos[n]
                answer += "L"

            elif right < left:
                right_now = hands_pos[n]
                answer += "R"
            else:
                if hand == "left":
                    left_now = hands_pos[n]
                    answer += "L"
                else:
                    right_now = hands_pos[n]
                    answer += "R"
        elif n in (1, 4, 7):
            answer += "L"
            left_now = hands_pos[n]
        else:
            answer += "R"
            right_now = hands_pos[n]
    return answer
