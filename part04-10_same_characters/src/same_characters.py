# Write your solution here
# You can test your function by calling it within the following block
def same_chars(string,a,b):

    if b>=len(string) or a>=len(string):
        return False
    
    if string[a] == string[b]:
        return True
    else:
        return False

if __name__ == "__main__":
    print(same_chars("abc",0,3))