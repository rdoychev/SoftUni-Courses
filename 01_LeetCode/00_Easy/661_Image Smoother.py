def image_smoother(img: list) -> list:
    rows = len(img)
    cols = len(img[0])
    filter_rc = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    filtered_img = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            avg = img[i][j]
            count = 1
            for k in filter_rc:
                nr, nc = i + k[0], j + k[1]
                if 0 <= nr < rows and 0 <= nc < cols:
                    avg += img[nr][nc]
                    count += 1

            filtered_img[i][j] = int(avg / count)

    return filtered_img

img1 = img = [[100,200,100],[200,50,200],[100,200,100]]
print(image_smoother(img1))