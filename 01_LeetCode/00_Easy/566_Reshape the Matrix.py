def matrix_reshape(mat: list, r: int, c: int) -> list:
    rows = len(mat)
    cols = len(mat[0])

    if rows * cols != r * c:
        return mat

    new_mat = [[0] * c for _ in range(r)]

    for i in range(rows):
        for j in range(cols):
            nidx = cols * i + j
            nr = nidx // c
            nc = nidx % c
            new_mat[nr][nc] = mat[i][j]

    return new_mat


mat1 = [[1, 2], [3, 4]]
r1 = 2
c1 = 2
print(matrix_reshape(mat1, r1, c1))
