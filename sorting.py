numbers = [67,82,91,3,27,41,2]
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        print("before", numbers)
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        print("after", numbers)
print(numbers)