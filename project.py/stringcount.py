s = input("enter a string: ")
find = input("enter char to be counted: ")

count = 0
for char in s:
    if char==find:
        count+=1
print(f"the count of {find} in {s} is {count}")