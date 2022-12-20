def length_of_longest(my_list) ->int:
    longest = my_list[0]
    for item in my_list:
        if len(item)>len(longest):
            longest=item

    return len(longest)

if __name__=="__main__":

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)
