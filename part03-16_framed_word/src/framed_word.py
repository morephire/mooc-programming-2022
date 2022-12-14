# Write your solution here
word = input("Word:")

if len(word) > 28:
    word= word[0:28]

line =30 * '*'
r_space = 15 -len(word) 
l_space = 15 - len(word)

sum = r_space + l_space

print(sum)

remaining = 30 - r_space - l_space

middle = " "*r_space+ word+" "*l_space

print(line)
print('*'+middle+'*')
print(line)