# Write your solution here
def chessboard(n):
    count = 0
    row_index = 0
    string = ""
    while count < n:

        if row_index == n:
            string += "\n"
            count += 1
            row_index=0
            if count == n:
                break

        if count%2==0:
            if row_index % 2 == 0:
                string += "1"
            else:
                string +="0"
        else:
            if row_index % 2 != 0:
                string += "1"
            else:
                string +="0"
        
        row_index+=1

    print(string.strip())


# Testing the function
if __name__ == "__main__":
    chessboard(3)
