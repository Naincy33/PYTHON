sample= input("Enter a string: ")
count = 0
for i in range(len(sample)):
    if(sample[i] in 'aeiouAEIOU'):
       count+=1
print("Number of vowels is: ", end="")
print(count)

    
