#Duplicates
numbers=[1,2,3,4,5,4,2,3,7,6,8,7]
duplicates=[]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
                   if numbers[i]==numbers[j] and numbers[i] not in duplicates:
                       duplicates.append(numbers[i])
print("Duplicate values are:",duplicates)
