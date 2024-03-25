from typing import List


def split_at_first(string: str, character: str | List[str]) -> str:
    to_return = ""
    if type(character) == str:
        for char in string:
            if char == character:
                break
            to_return += char
    else:
        for char in string:
            if char in character:
                break
            to_return += char
    return to_return
