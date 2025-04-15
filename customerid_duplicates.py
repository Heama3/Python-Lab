#Duplicates
customer_ids = [101, 102, 103, 101, 104, 102]
unique_customer_ids = []
for cid in customer_ids:
    if cid not in unique_customer_ids:
        unique_customer_ids.append(cid)

print(unique_customer_ids)
