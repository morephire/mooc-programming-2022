# NOTE
# THIS IS A NON WORKING SOLUTION

def squared(string: str,size : int):
    i = 0
    while i < size:
        if i % 2 == 0:
            row = string*size
        else:
            row = string*size
        # Remove extra characters at the end of the row
        print(row[0:size])
        i += 1


if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
