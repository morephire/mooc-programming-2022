# Write your solution here
# You can test your function by calling it within the following block
def first_word(sentece):
    array = sentece.split(" ")
    return array[0]
def second_word(sentece):
    array = sentece.split(" ")
    return array[1]
def last_word(sentece):
    array = sentece.split(" ")
    return array[-1]
    
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))