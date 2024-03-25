import os
import re
import sys
from typing import Any, Dict, List
from rich import print
from tools import handle_statement, split_at_first


def execute_command(phrase: str) -> bool:
	command = split_at_first(phrase, [" ", "(", ")"])
	phrase = phrase.removeprefix(command).strip()

	match command:
		case "print":
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
					variables[phrase_split[0]] = phrase_split[2][1:-1]
					print(f"{variables} //")
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

	#* Indent Calculation *#
	indent = 0
	while line.startswith("\t"):
		indent += 1
		line = line[1:]
	

	# line_split = [item for item in re.split(r"[\(\),]", line) if item != ""]
	# if len(line_split) == 0:
	# 	line_split.append("")
	# main_command = line_split[0]
	# print(line_split)
	
	# success = execute_command(line_split)

	success = execute_command(line)

	debug_line = f"{str(index).ljust(3)} |--{'---'*indent}> {line}"
	print(f"{debug_line.ljust(40)} {f'[green]{tick} SUCCESS[/green]' if success else f'[red]{cross} FAILURE[/red]'}")
