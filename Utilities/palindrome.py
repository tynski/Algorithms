def palindrome_index(word):
    n = len(word)
    for i in range(n//2+1):
        if word[i] != word[n-1-i]:
            if word[i] == word[n-2-i] and word[i+1] == word[n-3-i]:
                return n-1-i
            return i
    return -1

def is_palindrome(word):
    n = len(word)
    for i in range(n//2+1):
        if word[i] != word[n-1-i]:
            return False

    return True
