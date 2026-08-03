def matrix_reshape(mat: list, r: int, c: int) -> list:
    rows = len(mat)
    cols = len(mat[0])

    if rows * cols != r * c:
        return mat

    new_mat = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(rows):
        for j in range(cols):
            nidx = cols * i + j
            nr = nidx // c
            nc = nidx % c
            new_mat[nr][nc] = mat[i][j]

    return new_mat


mat1 = [[1, 2], [3, 4]]
r1 = 1
c1 = 4
print(matrix_reshape(mat1, r1, c1))
