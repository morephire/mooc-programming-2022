def no_vowels(string:str)-> str:
    vowels = "aeiou"
    for char in string:
        if char in vowels:
            string = string.replace(char,"")

    return string

if __name__ =="__main":

    my_string = "this is an example"
    print(no_vowels(my_string))
