from typing import Any, Dict, List
from rich import print as rprint

MODIFIERS = ["=", "+", "-"]

def set_type(item: Any, variables: Dict[str, Any]) -> Any:
	var_keys = list(variables.keys())
	if item in var_keys:
		item = f"\"{variables[item]}\"" if type(variables[item]) == str else variables[item]


	if str(item).isdigit():
		item = int(item)
	elif item.startswith('"') and item.endswith('"'):
		item = item[1:-1]
	else:
		rprint(f"  [red]Err:[/red] '{item}' is not recognised as a type")
		quit()
	return item


def get_types(statement: str, variables: Dict[str, Any]) -> List[Any]:
	to_return: List = []
	
	
	to_add = ""
	in_str = False
	for character in statement:
		if character in MODIFIERS and not in_str:
			to_add = set_type(to_add, variables)
			to_return.append(to_add)
			to_return.append(character)
			to_add = ""
			continue
		elif character == "\"":
			in_str = not in_str
		elif character == " " and not in_str:
			continue
		to_add += character

	to_return.append(set_type(to_add, variables))
		
	return to_return
		

def handle_statement(statement: str, variables: Dict[str, Any]) -> Any:
	to_return = None

	statement_typed = get_types(statement, variables)
	modifier = "="

	for part in statement_typed:
		match modifier:
			case "=":
				to_return = part
				modifier = None
			case "+":
				try:
					to_return += part
				except TypeError:
					to_return = str(to_return) + str(part)
				modifier = None
			case "-":
				to_return -= part
				modifier = None
		if part in MODIFIERS:
			modifier = part
	
	return to_return


if __name__ == "__main__":
	vars = {
	    "testi_1": 3,
	    "testi_2": 2,
	    "tests_1": "hi",
		"tests_2": "goodbye!"
	}
	statement_1 = "\"hi there! \" + tests_2"
	statement_2 = "2 + testi_2 - 3 + testi_1"

	for line in open("code/statement_test.txt", "r").readlines():
		print(handle_statement(line.strip(), vars))
