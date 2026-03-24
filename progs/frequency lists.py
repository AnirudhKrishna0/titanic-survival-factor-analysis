nums = [1, 2, 2, 3, 4]
count = {}
for n in nums:
    count[n] = count.get(n, 0) + 1
print(count)
