def snake_to_camel_case(s: str) -> str:
    words = s.split("_")
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return "".join(words)

print(snake_to_camel_case("snake_to_camel_case"))
