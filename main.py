import os
import re
import sys
from typing import Any, Dict, List
from rich import print
from tools import handle_statement, split_at_first, set_type


def execute_command(phrase: str) -> bool:
	command = split_at_first(phrase, [" ", "(", ")"])
	phrase = phrase.removeprefix(command).strip()

	match command:
		case "print":
			# print(f"//// {phrase} //// {phrase[1:-1]}")
			print(handle_statement(phrase[1:-1], variables))
		case "var":
			phrase_split = []
			current = ""
			is_str = False
			for character in phrase:
				if character == " " and not is_str:
					phrase_split.append(current)
					current = ""
					continue
				if character == "\"":
					is_str = not is_str

				current += character
			phrase_split.append(current)
				

			match phrase_split[1]:
				case "=":
					variables[phrase_split[0]] = set_type(phrase_split[2], variables)
					# print(f"{variables[phrase_split[0]]} //")
				case _:
					pass
		case _:
			return False
	return True


#* Read args *#
args = sys.argv[1:]
try:
	input_file = args[0]
except IndexError:
	print(f"[red]Err:[/red] Expected 'main.py <input_path: str>'\n     But recieved 'main.py{' ' if len(args) > 0 else ''}{' '.join(args)}'")
	quit()



#* Constants *#
string_regex = r"\(\"[a-zA-Z, ]+\"\)"
var_regex = r"\([, A-Za-z]+\)"

tick = "\u2713"
cross = "\u2717"


#* Interpreter Variables *#
variables: Dict[str, Any] = {}


for index, line in enumerate(open(input_file).readlines()):
	line = line.strip("\n")
	if line == "" or line.startswith("//"):
		continue

	#* Indent Calculation *#
	indent = 0
	while line.startswith("\t"):
		indent += 1
		line = line[1:]
	

	success = execute_command(line)

	debug_line = f"{str(index+1).ljust(3)} |--{'---'*indent}> {line}"
	# print(f"{debug_line.ljust(40)} {f'[green]{tick} SUCCESS[/green]' if success else f'[red]{cross} FAILURE[/red]'}")
