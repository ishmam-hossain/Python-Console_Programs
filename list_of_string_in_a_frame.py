
# expected output:
'''
*********
* Hello *
* World *
* in    *
* a     *
* frame *
*********
'''

def find_longest_word_size(s_list):
    longest_word = ''

    for word in s_list:
        if len(word) > len(longest_word):
            longest_word = word
    
    return len(longest_word)


s_list = [ "Hello", "World", "in", "a", "frame", "test" ]
frame_char = '*'

sz = find_longest_word_size(s_list)


for i in range(len(s_list)+2):
    if i == 1 or i == len(s_list) + 2:
        for star in range(sz+4):
            print '*'

    