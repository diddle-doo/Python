# check if the string is a palindrome
#noon
def palindrome(string):
    for char in range(len(string)):
        char_2=len(string)-char-1
        if string[char] == string[char_2]:
            return True
        else:
            return False

print(palindrome("civic"))
