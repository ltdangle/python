import re

def camel_to_snake_case(string:str)->str:
    words= re.split('(?=[A-Z])', string)
    return "_".join(words).lower().lstrip("_")

print(camel_to_snake_case("SnakeCaseText"))
