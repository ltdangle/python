def count_words(sentence: str) -> int:
    words = sentence.split(" ")
    return len(words)


print(count_words("Гаррі Поттер (англ. Harry Potter) — серія з семи фантастичних романів англійської письменниці."))
