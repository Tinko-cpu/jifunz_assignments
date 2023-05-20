# Write a python program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

def sentence_number(sentence):
    """This function will return the total number of character and number in your sentence"""
    my_alpha = 0
    my_number = 0
    for char in sentence:
        is_alpha = char.isalpha()
        is_number = char.isdigit()
        if is_alpha:
            my_alpha += 1
        elif is_number:
            my_number += 1
    return f"LETTERS {my_alpha}\nDIGITS {my_number}"


user_sentence = input("Enter your sentence? ")

result = sentence_number(user_sentence)
print(result)