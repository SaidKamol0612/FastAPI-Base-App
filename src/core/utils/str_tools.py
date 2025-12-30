def to_snake_case(input_str: str):
    """
    >>> to_snake_case(input_str="PascalCase")
    "pascal_case"
    >>> to_snake_case(input_str="camelCase")
    "camel_case"
    >>> to_snake_case(input_str="ThisIsFunny")
    "this_is_funny"
    """

    chars = []
    for idx, char in enumerate(input_str):
        if idx and char.isupper():
            nxt = idx + 1
            flag = nxt >= len(input_str) or input_str[nxt].isupper()
            if not (input_str[idx - 1].isupper() and flag):
                chars.append("_")
        chars.append(char.lower())
    return "".join(chars)


def pluralize(word: str) -> str:
    irregular = {
        "man": "men",
        "woman": "women",
        "child": "children",
        "tooth": "teeth",
        "foot": "feet",
        "mouse": "mice",
        "person": "people",
    }

    f_exceptions = {"roof", "belief", "chef", "chief"}

    if word.lower() in irregular:
        return irregular[word.lower()]

    if word.endswith("y") and word[-2].lower() not in "aeiou":
        return word[:-1] + "ies"

    if word.endswith(("s", "sh", "ch", "x", "z")):
        return word + "es"

    if word.endswith("fe") and word not in f_exceptions:
        return word[:-2] + "ves"

    if word.endswith("f") and word not in f_exceptions:
        return word[:-1] + "ves"

    return word + "s"
