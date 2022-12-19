# Write your solution here
n_items = int(input("How many items:"))
count = 1
list_items = []

while count <= n_items:
    item = int(input(f"Item {count}:"))
    list_items.append(item)
    count+=1

print(list_items)