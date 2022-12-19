#Assumption: both list has the same length
def list_sum(list1,list2) ->list:
    index = 0
    sum_list=[]
    while index < len(list1):
        sum_list.append(list1[index] + list2[index])
        index+=1
    
    return sum_list

# Other possible way to iterate would be
#
#  for in range(len(list1))
#       ....




if __name__=="__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))  # [8, 10, 12]

