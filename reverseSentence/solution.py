text = "Ola, tesntado aqui ok!"

def reverse(input_str):
    words = input_str.split(' ')
    words.reverse()
    return " ".join(words)

print(reverse(text))

'''

    Reverse a string words, but keep the ponctuation.



    example:

    'Hello, this is a sentence.' => 'sentence. a is this Hello,'

    Solution:

    Just split the string and reverse the list

'''
