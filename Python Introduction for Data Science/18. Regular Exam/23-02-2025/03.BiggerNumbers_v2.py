numbers = list(map(int, input().split()))

n = int(input())

print(" ".join(map(str, [num for num in numbers if num > n])))
