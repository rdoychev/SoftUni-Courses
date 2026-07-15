matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0]
]

node1 = 0
node2 = 2
chk_if_connected = False
if matrix[node1][node2]:
    chk_if_connected = True

print(chk_if_connected)
