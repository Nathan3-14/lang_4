from typing import Any, Dict, List

MODIFIERS = ["=", "+", "-"]

def set_type(item: Any, variables: Dict[str, Any]) -> Any:
	var_keys = list(vars.keys())
	if item in var_keys:
		print(f" {item}  is in  {var_keys}")
		print(f"{variables[item]}")
		print(f"{str(variables[item]).isdigit()}")
		item = variables[item]
	else:
		print(f" {item}  is not in  {var_keys}")


	if str(item).isdigit():
		item = int(item)
	elif item.startswith('"') and item.endswith('"'):
		print(f"{item} starts with \"")
		item = item[1:-1]
	else:
		print(f"{item} is not valid type")
	return item


def handle_statement(statement: str, variables: Dict[str, Any]) -> List[Any]:
	to_return: List = []

	var_keys = list(variables.keys())
	
	
	to_add = ""
	for character in statement:
		if character in MODIFIERS:
			to_add = set_type(to_add, variables)
			to_return.append(to_add)
			to_return.append(character)
			to_add = ""
			continue
		elif character == " ":
			continue
		to_add += character

	to_return.append(set_type(to_add, variables))
		
	return to_return
		
	

if __name__ == "__main__":
	vars = {
	    "testi_1": 3,
	    "testi_2": 2,
	    "tests_1": "hi"
	}
	
	print(handle_statement("1 + testi_2 + testi_1", vars))
	print(handle_statement("\"hi\" + tests_1", vars))
