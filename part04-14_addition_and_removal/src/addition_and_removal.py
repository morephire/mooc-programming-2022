my_list = []
value = 1

while True:
    print(f"The list is now {my_list}")
    choice = input("a(d)d, (r)emove or e(x)it:")

    if choice == "d":
        my_list.append(value)
        value += 1
    elif choice == "r":
        my_list.pop(len(my_list)-1)
        value-=1
    elif choice == "x":
        break
    else:
        print("invalid choice")

print("Bye!")