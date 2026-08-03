def distribute_candies(candyType: list) -> int:
    num_candies = len(candyType)
    unique_candies = len(set(candyType))

    if num_candies // 2 >= unique_candies:
        return unique_candies

    return num_candies // 2


candyType1 = [1,1,2,3]
print(distribute_candies(candyType1))