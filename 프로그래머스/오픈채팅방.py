def solution(record):
    answer = []
    user = dict()
    save = []

    for r in record:
        r = r.split(" ")

        if r[0] == "Enter":
            user[r[1]] = r[2]
            save.append((r[0], r[1]))
        elif r[0] == "Leave":
            save.append((r[0], r[1]))
        elif r[0] == "Change":
            user[r[1]] = r[2]

    for s in save:
        if s[0] == "Enter":
            answer.append(user[s[1]] + "님이 들어왔습니다.")
        elif s[0] == "Leave":
            answer.append(user[s[1]] + "님이 나갔습니다.")

    return answer
