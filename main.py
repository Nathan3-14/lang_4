import os
import re
import sys
from typing import Any, Dict, List
from rich import print
from tools import handle_statement, split_at_first, set_type, split_at_space


def execute_command(phrase: str, indent: int) -> bool:
	command = split_at_first(phrase, [" ", "(", ")"])
	phrase = phrase.removeprefix(command).strip()

	match command:
		case "print":
			print(handle_statement(phrase[1:-1], variables))
		case "var":
			phrase_split = split_at_space(phrase)

			match phrase_split[1]:
				case "=":
					# make this handle '3 + 2' and similar
					variables[phrase_split[0]] = handle_statement(" ".join( phrase_split[2:]), variables)
				case _:
					pass
		case "if":
			phrase_split = split_at_space(phrase[1:-1])

			current = False
			current_link = "||"
			current_comparison: List = []
			for index, part in enumerate(phrase_split):
				done = index+1 == len(phrase_split)

				if part in ["&&", "||"]:
					current_link = part
					continue
				
				if len(current_comparison) > 0:
					if (current_comparison[-1] not in ["=="]) and (part != "=="):
						current_comparison[-1] += part
					else:
						current_comparison.append(part)
				else:
					current_comparison.append(part)
				# print(f"Current comparison: {current_comparison}")
				# mmake itr so it handles up to the '==' instead of just the middle
				if done:
					temp = False
					match current_comparison[1]:
						case "==":
							temp = handle_statement(current_comparison[0], variables) == handle_statement(current_comparison[2], variables)

					match current_link:
						case "&&":
							current = temp and current
						case "||":
							current = temp or current
					current_comparison = []
			
			if_bools[indent+1] = current
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
if_bools = {0: True}


for index, line in enumerate(open(input_file).readlines()):
	line = line.strip("\n")
	if line == "" or line.startswith("//") or line.startswith("%"):
		continue

	#* Indent Calculation *#
	indent = 0
	while line.startswith("\t"):
		indent += 1
		line = line[1:]

	if indent == 0:
		if_bools[indent+1] = False
	if if_bools[indent]:
		success = execute_command(line, indent)

	debug_line = f"{str(index+1).ljust(3)} |--{'---'*indent}> {line}"
	# print(f"{debug_line.ljust(40)} {f'[green]{tick} SUCCESS[/green]' if success else f'[red]{cross} FAILURE[/red]'}")
