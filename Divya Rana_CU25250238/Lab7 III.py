arr = [2, 1, 5, 2, 3, 2]
target = 7
 
left = 0
total = 0
min_length = len(arr) + 1

for right in range(len(arr)):
    total += arr[right]

    while total > target:
        length = right - left + 1
        min_length = min(min_length, length)

        total -= arr[left]
        left += 1

if min_length == len(arr) + 1:
    print(-1)
else:
    print(min_length)