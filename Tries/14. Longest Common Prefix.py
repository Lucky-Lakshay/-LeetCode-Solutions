#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

def longestCommonPrefix(strs):
    if not strs:
        return ""

    strs.sort()
    first = strs[0]
    last = strs[-1]
    i = 0

    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return first[:i]

print(longestCommonPrefix(["flower","flow","flight"]))    
print(longestCommonPrefix(["dog","racecar","car"]))    