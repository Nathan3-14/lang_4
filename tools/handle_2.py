from typing import Any, Dict, List

MODIFIERS = ["=", "+", "-"]

def set_types(statement: str) -> List[Any]:
    to_return: List = []


    to_add = ""
    for character in statement:
        if character in MODIFIERS:
            if to_add.isdigit():
                to_add = int(to_add)
            elif to_add.startswith("\"") and to_add.endswith("\""):
                print(f"{to_add} starts with \"")
                to_add = to_add[1:-1]
            else:
                print(f"'{to_add}' doesn't start with \"")
                print(f"{to_add} is not valid type")

            to_return.append(to_add)
            to_return.append(character)
            to_add = ""
            continue
        
        to_add += character
    to_return.append(to_add)
    
    return to_return


def handle(statement: str, variables: Dict[str, Any]) -> Any:
    variable_keys = list(variables.keys())
    statement_split = statement.split(" ")

    current = None

    modifier = "="

    for item in statement_split:
        if item in variable_keys:
            alter = variables[item]
        elif item in MODIFIERS:
            modifier = item
            alter = None
        else:
            alter = item

        
        match modifier:
            case "=":
                current = item
            case "+":
                current += item


        print(f"  {str(item).ljust(10)} // Current: {str(current).ljust(10)} // Alter: {str(alter).ljust(10)}")


    return current


if __name__ == "__main__":
    # vars = {
    #     "testi_1": 3,
    #     "testi_2": 2,
    #     "tests_1": "hi"
    # }
    # statement = "1 + test-i_1"

    # print(handle(statement, vars))
    print(set_types("1 + testi_2 + testi_1"))
    print(set_types("\"hi\" + tests_1"))
