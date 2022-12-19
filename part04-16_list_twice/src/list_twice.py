# Write your solution here
items = []
while True:
    item = int(input("New item:"))

    if item == 0:
        break

    items.append(item)
    print("The list now:",items)
    print("The list in order:",sorted(items))

print("Bye!")