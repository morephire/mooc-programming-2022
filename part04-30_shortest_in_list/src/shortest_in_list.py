def shortest(my_list) -> str:
    shortest = my_list[0]
    for item in my_list:
        if len(item) < len(shortest):
            shortest = item

    return shortest


if __name__ == "__main__":

    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)
