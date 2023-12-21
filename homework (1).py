print("Problem 1")
print("-----------")

string = input("Give me a word: ")
for letter in string:
    if letter == 'A' or letter == 'a':
        print(letter)
print()

print("Problem 2")
print("-----------")

def chain(word1, word2):
    if word1[0] == word2[len(word2) - 1]:
        print(word2, word1)
    elif word2[0] == word1[len(word1) - 1]:
        print(word1, word2)
    else:
        print('NO CHAIN')

chain('dog', 'toad')
chain('cat', 'take')
chain('cake', 'rat')
print()

print("Problem 3")
print("-----------")

word1 = input('Give me a word: ')
word2 = input('Give me another word: ')
if word1[len(word1) - 2:] == word2[len(word2) - 2:]:
    print(word1, 'and', word2, 'rhyme.')
else:
    print(word1, 'and', word2, 'DO NOT rhyme.')
print()

# print("Problem 4")      ---> This doesn't work
# print('-----------')

# def secret_message(encoded1, encoded2):
#     counter = 0
#     for i in range(1, (len(encoded1) + len(encoded2))+1):
#         if i % 2 == 0:
#             counter = counter + 1
#             print(encoded1[counter - 1])
#         elif i % 2 > 0:
#             counter = counter + 1
#             print(encoded2[counter - 1])
# secret_message('Pto', 'yhn')
print("Problem 5")
print("-----------")
word = input("Give me a word: ")
for i in range(len(word)):
    letter = word[i]
    print(i * '.' + letter)
print()

print("End of Homework")