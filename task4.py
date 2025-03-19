def solve(array: list[float]) -> tuple[int, int, int]:
    s = 0  # sum
    p = 1  # product
    c = 0  # count of positive
    for x in array:
        s += x
        p *= x
        if x > 0:
            c += 1

    return s, p, c


if __name__ == "__main__":
    arr = [0.4, -3.14, 13.0, 3.1, -0.31, 0.11, -7.0]
    print(solve(arr))
