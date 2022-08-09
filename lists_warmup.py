numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0] # Value: 3
numbers[-1] #Value: 2
numbers[3] #Value: 1
numbers[:-1] #Value: [3, 1, 4, 1, 5, 9]
numbers[3:4] #Value: [1]
5 in numbers #True
7 in numbers #False
"3" in numbers #False
numbers + [6, 5, 3] #Value: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers = ["ten", 1, 4, 1, 5, 9, 1]
print(numbers[-5::1])
print(9 in numbers)