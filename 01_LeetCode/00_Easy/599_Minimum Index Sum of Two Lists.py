def find_restaurant(list1: list, list2: list) -> list:
    list2_dic = {val: idx for idx, val in enumerate(list2)}
    min_idx_sum = float('inf')
    out = []

    for idx, word in enumerate(list1):
        if word in list2_dic.keys():
            tmp = idx + list2_dic[word]

            if tmp < min_idx_sum:
                out = [word]
                min_idx_sum = tmp
            elif tmp == min_idx_sum:
                out.append(word)

    return out


list1a = ["happy","sad","good"]
list2a = ["sad","happy","good"]
print(find_restaurant(list1a, list2a))