def find_relative_ranks(score: list) -> list:
    score_len = len(score)
    answer = [""] * score_len
    score_place = {}

    for i in range(len(score)):
        score_place[score[i]] = i

    score.sort(reverse=True)

    for idx in range(len(score)):
        place = score_place[score[idx]]
        if idx == 0:
            answer[place] = "Gold Medal"
        elif idx == 1:
            answer[place] = "Silver Medal"
        elif idx == 2:
            answer[place] = "Bronze Medal"
        else:
            answer[place] = str(idx + 1)

    return answer

score1 = [10,3,8,9,4]
print(find_relative_ranks(score1))