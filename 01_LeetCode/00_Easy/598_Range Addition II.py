def max_count(m: int, n: int, ops: list[list[int]]) -> int:
    ops_len = len(ops)
    if ops_len == 0:
        return m * n

    min1 = min(x[0] for x in ops)
    min2 = min(x[1] for x in ops)

    return min1 * min2


m1 = 18
n1 = 3
ops1 = [[16,1],[14,3],[14,2],[4,1],[10,1],[11,1],[8,3],[16,2],[13,1],[8,3],[2,2],[9,1],[3,1],[2,2],[6,3]]
print(max_count(m1, n1, ops1))