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

def split_at_space(string: str) -> List[str]:
	to_return: List[str] = []

	current = ""
	is_str = False
	for character in string:
		if character == " " and not is_str:
			to_return.append(current)
			current = ""
			continue
		if character == "\"":
			is_str = not is_str

		current += character
	to_return.append(current)
	
	return to_return
