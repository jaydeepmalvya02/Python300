def generateMatrix(n):
    k = n * n
    ans = [[0] * n for _ in range(n)]

    minr = 0
    minc = 0
    maxr = n - 1
    maxc = n - 1
    count = 1
    while count <= n * n:

        # top
        i = minr
        j = minc
        while j <= maxc and count <= n * n:
            ans[i][j] = count

            j += 1
            count += 1
        minr += 1

        # right
        i = minr
        j = maxc
        while i <= maxr and count <= n * n:
            ans[i][j] = count

            i += 1
            count += 1
        maxc -= 1
        # bottom
        i = maxr
        j = maxc
        while j >= minc and count <= n * n:
            ans[i][j] = count

            j -= 1
            count += 1
        maxr -= 1

        # left
        i = maxr
        j = minc
        while i >= minr and count <= n * n:
            ans[i][j] = count

            i -= 1
            count += 1
        minc += 1

    print(ans)


n = 3
generateMatrix(n)
