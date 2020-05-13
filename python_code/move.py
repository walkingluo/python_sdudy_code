def movingCount(m: int, n: int, k: int) -> int:
    count = 0
    for i in range(m):
        if i >= 10:
            i = i // 10 + i % 10
        for j in range(n):
            if j >= 10:
                j = j // 10 + j % 10
            print(i, j)
            if i + j <= k:
                count += 1
    return count


movingCount(16, 8, 4)
