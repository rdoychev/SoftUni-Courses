def josephus(people: int) -> int:
    # for k = 2
    # import math
    # largest_power_of_two = 2 ** math.floor(math.log2(people))
    # return 2 * (people - largest_power_of_two) + 1

    # NO tracking of killed people
    # k = 2
    # survivor = 0  # Base case for n = 1 in 0-based indexing
    # for i in range(2, people + 1):
    #     survivor = (survivor + k) % i
    # return survivor + 1  # Convert to 1-based position

    # Tracking of killed people
    k = 2
    people = list(range(1, people + 1))
    idx = 0
    elimination_order = []

    while len(people) > 1:
        # Calculate the index of the person to eliminate, adjusting for 1 step back
        idx = (idx + k - 1) % len(people)
        # Record who is eliminated
        elimination_order.append(people.pop(idx))

    return people[0], elimination_order


num_people = 7
print(josephus(num_people))
