lingth, width, c = map(int, input().split())

count = 0
count += lingth / c
if count is not int:
    count += 1
    count = int(count)
count += width / c
if count is not int:
    count += 1
    count = int(count)
print(count)
