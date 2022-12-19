def even_numbers(numbers:list)->list:
    even_numbers=[]
    for number in numbers:
        if number%2==0:
            even_numbers.append(number)

    return even_numbers


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
