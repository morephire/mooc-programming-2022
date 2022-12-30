def everything_reversed(words:list) -> list:
    reversed_list =[]
    for word in words:
        reversed_list.append(word[::-1])

    return reversed_list[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
