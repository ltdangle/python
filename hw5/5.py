# 5. Read the string and find its longest consecutive symbol.
#
# Example
#
# Input: 'aaaabchjjjjjswwwwwwwxyzaaaaaa'
#
# Output: `Longest consecutive symbol: w`
s = "aaaabchjjjjjswwwwwwwxyzaaaaaa"
i = 1
max_len = 0
max_symb = ""
conseq = ""
while i < len(s):
    if s[i - 1] == s[i]:
        conseq = conseq + s[i]
        if len(conseq) > max_len:
            max_len = len(conseq)
            max_symb = s[i - 1]
    else:
        conseq = s[i]
    i = i + 1

print(f"Longest consecutive symbol: {max_symb}")
