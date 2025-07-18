def is_palindrome(word):
    return word == word[::-1]

def is_near_palindrome(text):
    i = 0
    j = len(text) - 1
    while i < j:
        if text[i] != text[j]:
            without_left = text[i+1:j+1]
            without_right = text[i:j]

            if is_palindrome(without_left) or is_palindrome(without_right):
                return True
            else:
                return False
        i += 1
        j -= 1

    return True

print(is_near_palindrome("racecar"))