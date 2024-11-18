data={"mango":4,"apple":3,"banana":9}
sorted_items_asc=dict(sorted(data.items()))
sorted_items_desc=dict(sorted(data.items(),reverse='True'))
print("Ascending order : ",sorted_items_asc)
print("Descending order : ",sorted_items_desc)

