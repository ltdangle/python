# Write a function called `unique_characters` that takes in a string s and returns a Boolean value indicating whether or not all the characters in s are unique.
# For example, the string "abcdefg" has unique characters, but the string "abcdeff" does not.
def unique(s: str) -> bool:
    for i in range(len(s)):
        for k in range(len(s)):
            if i == k:
                continue
            if s[i] == s[k]:
                return False
    return True


print(unique("abcdefg"))
print(unique("abcdeff"))
