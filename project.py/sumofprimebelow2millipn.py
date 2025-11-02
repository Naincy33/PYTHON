sum=0
for i in range(1,2000000, +1):
    count=0
    for j in range (1, i+1,+1):
        if i%j==0:
            count += 1
    if count == 2:
        sum = sum+j
print(sum)