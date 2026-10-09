def solve():
    N = int(input())
    A = list(map(int, input().split()))

    positive = False
    negative = False
    # Check positive and negative elements
    for i in range(N):
        if A[i] > 0:
            positive = True
        elif A[i] < 0:
            negative = True

    # If both positive and negative exist
    if positive and negative:
        return -1

    # Count operations
    operations = 0

    for i in range(N):
        operations = operations + abs(A[i])

    return operations


print("Input:")

T = int(input())

answers = []

for i in range(T):
    answer = solve()
    answers.append(answer)

print("Output:")

for answer in answers:
    print(answer)
#2
#1
#-2
#2
#1 -1
