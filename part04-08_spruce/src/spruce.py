# Write your solution here
def spruce(size):
    print("a spruce!")
    
    row = "*"
    i = size
    while i > 0:
        i -= 1
        print(" "* i + row)
        row += "**"
        
    
    print(" "*(size-1)+"*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)