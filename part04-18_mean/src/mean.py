# Write your solution here
def summation (my_list):
    index = 0
    sum=0
    while index <= len(my_list)-1:
        sum += my_list[index]
        index+=1
    return sum

def mean(my_list: list) -> float :
    return summation(my_list)/len(my_list)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)