from codingTest import CheckTime


@CheckTime.CheckTime
def solution(s):
    answer = ""
    num_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    save_alpha = ""
    for i in s:
        if i.isdigit():
            answer += i
        else:
            save_alpha += i
            if save_alpha in num_dict:
                answer += num_dict[save_alpha]
                save_alpha = ""
    if save_alpha:
        answer += num_dict[save_alpha]
    return int(answer)


if __name__ == "__main__":
    solution("one4seveneight")
    solution("23four5six7")
    solution("2three45sixseven")
    solution("123")
