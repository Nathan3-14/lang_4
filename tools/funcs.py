from typing import Any, Dict


def handle_statement(statement: str, vars: Dict[str, Any]) -> Any:
    var_keys = list(vars.keys())
    statement_split = statement.split(" ")

    modifiers = {
        "=": "equal",
        "+": "add",
        "-": "subtract",
        "*": "multiply",
        "/": "divide"
    }
    modifier_keys = list(modifiers.keys())
    modifier = modifiers["="]

    current = None
    to_modify = None

    for item in statement_split:
        if item.isdigit():
            item = int(item)

        if item in var_keys:
            to_modify = vars[item]
        elif item in modifier_keys:
            modifier = modifiers[item]
            to_modify = None
        else:
            to_modify = item
        
        if to_modify == None:
            continue

        match modifier:
            case "equal":
                current = to_modify
            case "add":
                current += to_modify
            case "subtract":
                current -= to_modify
            case "multiply":
                current *= to_modify
            case "divide":
                current /= to_modify
        print(f"    DEBUG: {str(item).ljust(10)} //  {str(modifier).ljust(10)} //  {str(to_modify).ljust(10)} //  {current}")
    return current
    

if __name__ == "__main__":
    vars = {
        "test": 3,
        "test_2": 5
    }

    test_statement = "test + 2 + test_2 - 5"
    print(handle_statement(test_statement, vars))