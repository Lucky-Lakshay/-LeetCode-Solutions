# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# SOlUTION 1
# def lengthOfLastWord(s):
#         s = s.strip().split()
#         return len(s[-1])

def lengthOfLastWord(s):
    length = 0
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1  # skip trailing spaces
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1  # count the word
    return length

print(lengthOfLastWord(s = "Hello World"))        
print(lengthOfLastWord(s = "   fly me   to   the moon  "))        
print(lengthOfLastWord(s = "luffy is still joyboy"))        