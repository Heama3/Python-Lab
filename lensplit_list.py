#Length and Split
original_list=[1,1,2,3,4,4,5,1]
#Length
split_index=3
#Splitting
first_part=original_list[:split_index]
second_part=original_list[split_index:]

print("original list:",original_list)
print("Length of the first part of the string:",split_index)
print("Splitted the given list into two parts,as:",(first_part,second_part))
