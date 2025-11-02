def square_sum(numbers):
    total=0
    
    for num in numbers:

        total+= num*num
    return total

numbers = [1,2,2]
result= square_sum(numbers)
    
print(result) 

