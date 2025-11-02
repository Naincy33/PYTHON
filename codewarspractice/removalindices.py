def getRemovableIndices(str1, str2): 
    removal_indices = []
    for i in range(len(str1)):  
        new_str = str1[:i] + str1[i+1:]
        if new_str == str2:
            
            removal_indices.append(i)

   
    return removal_indices if removal_indices else[-1]


str1 = "abdgggda"
str2 = "abdggda"

result = getRemovableIndices(str1, str2)
print(result)
