#Question 1
name = input("Enter your name: ")
out_file = open("name.txt", 'w')
print(f"{name}", file= out_file)
out_file.close()

#Question 2
in_file = open("name.txt", 'r')

print(f"Your name is {in_file.read()}")

in_file.close()

#Question 3
sum = 0
f = open("numbers.txt")
print(f.readline())
print(f.readline())
with open("numbers.txt") as f:
    for x in f:
        x = x.strip()
        sum = int(x) - 341
print(sum)


f.close()


#Question 4
input_file = open("numbers.txt", 'r')
sum = 0
with open("numbers.txt") as input_file:
    for line in input_file:
        line = line.strip()
        sum = sum + int(line) #convert into integer
print(sum)

input_file.close()





