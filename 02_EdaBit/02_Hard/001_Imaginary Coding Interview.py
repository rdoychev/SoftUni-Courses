def interview(lst, tot):
    total_question_time = sum(lst)

    if len(lst) != 8 or tot > 120 or total_question_time > 100:
        return "disqualified"

    if lst[0] > 5 or lst[1] > 5 or lst[2] > 10 or lst[3] > 10 or \
            lst[4] > 15 or lst[5] > 15 or lst[6] > 20 or lst[7] > 20:
        return "disqualified"

    return "qualified"


inp = [5, 5, 10, 10, 15, 15, 20, 20]
t1 = 130

print(interview(inp, t1))
