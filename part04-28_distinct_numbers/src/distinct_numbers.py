def distinct_numbers(list:list) -> list:

    new = sorted(list)
    for number in list:
        if new.count(number)>1:
            new.remove(number)

    return new

if __name__ == "__main__":
    my_list = [3, 2, 1, 3, 2, 1, 3, 2, 1]
    print(distinct_numbers(my_list))  # [1, 2, 3]
