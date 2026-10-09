# Input N and K
N, K = map(int, input("Enter N and K: ").split())

# Input array
arr = list(map(int, input("Enter the array: ").split()))

# Find sum of first K elements
window_sum = sum(arr[:K])
max_sum = window_sum

# Sliding window
for i in range(K, N):
    window_sum = window_sum + arr[i] - arr[i - K]

    if window_sum > max_sum:
        max_sum = window_sum

print("Maximum sum:", max_sum)
# 6 3 
# 2 1 5 1 3 2 