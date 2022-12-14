# Copy here code of line function from previous exercise and use it in your solution
def line(times, string):
    if string == "":
        print("*"*times)
    else:
        print(string[0]*times)

def shape (size1,character1,size2,character2):
    
    #shaping triangle
    i = 0 
    while i < size1:
        i += 1
        line(i, character1)
    
    #shaping rectangle
    j =0
    while j < size2:
        j += 1
        line(size1,character2)
        


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")