def count_words(sentence: str) -> int:
    words = sentence.split(" ")
    return len(words)


print(count_words("This sentense has five words"))
