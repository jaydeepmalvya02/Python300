matrix=[
    [1,2,3,11],
    [4,5,6,22],
    [7,8,9,33],
    [12,13,14,15]
]






m = len(matrix)
n = len(matrix[0])
count = 0
ans = []
minr = 0
minc = 0
maxr = m - 1
maxc = n - 1
t=m*n
while count < t:

    # top
    i = minr
    j = minc
    while j <= maxc and count < t:
        ans.append(matrix[i][j])
        j += 1
        count += 1
    minr += 1
    # right
    i = minr
    j = maxc
    while i <= maxr and count < t:
        ans.append(matrix[i][j])
        count += 1
        i += 1
    maxc -= 1

    # bottom
    i = maxr
    j = maxc
    while j >= minc and count < t:
        ans.append(matrix[i][j])
        j -= 1
        count += 1
    maxr -= 1

    # left
    i = maxr
    j = minc
    while i >= minr and count < t:
        ans.append(matrix[i][j])
        count += 1
        i -= 1
    minc += 1
print(*ans)
    # bottom
    # left