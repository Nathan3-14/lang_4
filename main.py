import os
import re
import sys
from typing import Any, List
from rich import print


def execute_command(words: List[Any]) -> bool:
	command = words[0]
	match command:
		case "print":
			print(words[1])
			if (
				re.match(var_regex, words[1]) != None
				or
				re.match(string_regex, words[1]) != None
			):
				return False
			print(words[1])
	return True


string_regex = r"\(\"[a-zA-Z, ]+\"\)"
var_regex = r"\([, A-Za-z]+\)"

tick = "\u2713"
cross = "\u2717"


for index, line in enumerate(open("code/code.txt").readlines()):
	line = line.strip("\n")

	indent = 0
	while line.startswith("\t"):
		indent += 1
		line = line[1:]

	line_split = [item for item in re.split(r"[\(\),]", line) if item != ""]
	if len(line_split) == 0:
		line_split.append("")
	main_command = line_split[0]
	print(line_split)
	
	success = execute_command(line_split)

	debug_line = f"{str(index).ljust(3)} |--{'---'*indent}> {line}"
	print(f"{debug_line.ljust(40)} {f'[green]{tick} SUCCESS[/green]' if success else f'[red] {tick}FAILURE[/red]'}")
