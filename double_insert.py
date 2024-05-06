def bilinear_interpolation(image):
    h, w = image.shape
    new_h = h * 2
    new_w = w * 2
    output = [[0.0] * new_w for i in range(new_h)]

    for i in range(new_h):
        x = i / 2
        x1 = int(x)
        x2 = min(h - 1, x1 + 1)

        for j in range(new_w):
            y = j / 2
            y1 = int(y)
            y2 = min(w - 1, y1 + 1)

            f11 = image[x1][y1]
            f21 = image[x2][y1]
            f12 = image[x1][y2]
            f22 = image[x2][y2]

            output[i][j] = (f11 * (x2 - x) * (y2 - y)
                            + f21 * (x - x1) * (y2 - y)
                            + f12 * (x2 - x) * (y - y1)
                            + f22 * (x - x1) * (y - y1))
    return output