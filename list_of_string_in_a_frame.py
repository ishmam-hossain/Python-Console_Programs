
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


def putting_in_a_frame(s_list):
    for i in range(len(s_list)+2):
        if i == 0 or i == len(s_list) +1:
            print '*'*(sz+4)
        else:
            print('* ' + s_list[i-1] + ' '*(sz + 1 -len(s_list[i-1])) + '*'  )



s_list = [ "Hello", "World", "in", "a", "frame", "test", "another", "new" ]

sz = find_longest_word_size(s_list)
putting_in_a_frame(s_list)

    
