def most_common_character(string:str) -> str:
    most_common_char= string[0]
    for char in string:
        if string.count(char) > string.count(most_common_char):
            most_common_char = char

    return most_common_char


if __name__ == "__main__":

    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
