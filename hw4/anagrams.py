def anagram(s1: str, s2: str) -> bool:
    s1_list = sorted(list(s1))
    s2_list = sorted(list(s2))
    if s1_list == s2_list:
        return True
    return False


print(anagram("listen", "silent"))
print(anagram("hello", "world"))
