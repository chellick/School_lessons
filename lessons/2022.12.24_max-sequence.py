def max_sequence(arr):
    maxim = 0
    summ = 0
    count = 0
    for i in range(len(arr) - 1):
        summ += arr[i] + arr[i + 1]
        if maxim < summ:
            maxim = summ
    for h in arr:
        if h < 0:
            count += 1
    if count == len(arr) or len(arr) == 0:
        return 0
    else:
        return maxim
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))