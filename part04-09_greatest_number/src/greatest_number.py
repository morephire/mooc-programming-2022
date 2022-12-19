# Write your solution here
# You can test your function by calling it within the following block
def greatest_number(a,b,c):
    great = a
    
    if b>great and b>c:
        great =b
    elif c> great and c>b:
        great =c

    return great

if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)