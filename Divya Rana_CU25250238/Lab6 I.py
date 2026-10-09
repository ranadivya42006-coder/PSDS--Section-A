arr = [5, 6, -3, 8, 1, 9, 2]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            if arr[i] + arr[j] + arr[k] == 0:
                print(arr[i], arr[j], arr[k])