import random
content = []


def list_reduction(char, pos, dict):

    dict1 = dict[:]
    dict2 = [x for x in dict1 if  x[pos]==char]
    return dict2

def list_removal_yellow(char, pos, dict):

    dict1 = dict[:]
    dict2 = [x for x in dict1 if  x[pos]!=char]
    return dict2

def list_reduction_yellow(char, pos, dict):

    dict1 = dict[:]
    dict2 = [x for x in dict1 if char in x]
    return dict2

def check_input(word):
    '''checks if all elements in list 1 is in list 2'''
    if word.isalpha() == True:
        if len(word) == 5:
            return True
        else:
            return "Please input 5 letter words"
    elif word == "done":
        return "Congratulations"
    else:
        return "Please input alphabets"


def remove_element_from_dict(char,dict):
    dict1 = dict[:]
    dict2 = [x for x in dict1 if char not in x]
    return dict2

def input_format(input):
    return [int(x) for x in str(input)]

with open('data\data.txt') as f:
    lines = f.readlines()
    for x in lines:
        content.append(x)

for x in range(len(content)):
    content[x] = content[x][:len(content[x])-1].lower()



iter = 0


alphabet_filter = [x for x in content if  x.isalpha()]
length_filter = [x for x in alphabet_filter if  len(x)==5]
final_filter = [x for x in length_filter if  len(set(x)) == len(x)]

while True and iter<7:
    if iter == 0:
        first_word = input("Enter your first guess: ")
        if check_input(first_word) == True:
            green = input_format(input("Enter position of the green characters: "))
            yellow = input_format(input("Enter position of the yellow characters: "))
            black = input_format(input("Enter position of the black characters: "))
            if black != '':
                for i in black:
                    word_list = remove_element_from_dict(first_word[i-1],final_filter)
            if green != '':
                for i in green:
                    word_list = list_reduction(first_word[i-1], i-1,word_list)
            if yellow != '':
                for i in yellow:
                    word_list = list_removal_yellow(first_word[i-1], i-1, word_list)
            if yellow != '':
                for i in yellow:
                    word_list = list_reduction_yellow(first_word[i-1], i-1, word_list)
            iter = iter+1
            print("The possible words currently are: \n")


            print(word_list)
        else:
             check_input(first_word)
    else:
        word = input("Enter your next guess: ")
        if check_input(first_word) == True:
            green = input_format(input("Enter position of the green characters: "))
            yellow = input_format(input("Enter position of the yellow characters: "))
            black = input_format(input("Enter position of the black characters: "))
            if black != '':
                for i in black:
                    word_list = remove_element_from_dict(word[i-1],word_list)
            if green != '':
                for i in green:
                    word_list = list_reduction(word[i-1], i-1,word_list)
            if yellow != '':
                for i in yellow:
                    word_list = list_removal_yellow(word[i-1], i-1, word_list)
            if yellow != '':
                for i in yellow:
                    word_list = list_reduction_yellow(word[i-1], i-1, word_list)
            iter = iter+1
            print("The possible words currently are: \n")
            print(word_list)



