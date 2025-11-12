def count_words(file):
    with open(file) as f:
        file_contents = f.read()

    words = file_contents.split()
    word_count = 0 
    for word in words:
        word_count += 1
        
    return word_count, file_contents

def count_characters(file_contents):
    char_count = {}
    for i in range(len(file_contents)):
        char = file_contents[i].lower().strip()
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1

    return char_count

def sort_dict(char_count):
    sorted_dict = dict(sorted(char_count.items(), key= lambda x:x[1], reverse=True))
    
    return sorted_dict
    
