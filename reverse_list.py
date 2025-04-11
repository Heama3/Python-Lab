#Traversing list in reverse order
colors=['red','green','white','black']
print("Traverse the list in reverse order with original indexes:")
for i in range(len(colors)-1,-1,-1):
    print(f"Index{i}:{colors[i]}")
