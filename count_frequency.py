# Return list (word_frequency) of pairs (word,frequency) in 
# array (word_list). As input goes list of words (word_list).

def count_frequency(word_list):
    word_frequency = []
    for new_word in word_list:
        for unique_word in word_frequency:
            if new_word == unique_word[0]:
                unique_word[1] += 1
                break
        word_frequency.append([new_word,1])
    return word_frequency