
# English to Pig Latin
# input:   this is another line
# output:  histay siay notheraay inelay

# Pig Latin to English 
# input:   histay siay notheraay inelay
# output:  this is another line


def english_to_pig_latin(words):
    
    res = ''

    for word in words:
        if len(word) > 1:
            res += word[1:] + word[0] + 'ay '
        else:
            res += word + ' '

    print(res)
    pig_latin_to_english(res.split(' '))


def pig_latin_to_english(words):

    res = ''
    words = words[:-1]

    for word in words:
        res += word[-3] + word[:-3] + ' '
    
    print(res)



words = raw_input("Enter: ").split(' ')
english_to_pig_latin(words)
