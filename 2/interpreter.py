import re

class BarebonesSyntaxError(Exception):
	def __init__(self,message):
		super().__init__(message)		

	with open(path,"r") as f:
		pureText = f.read()
		commands = pureText.split(";")
		program = [""]
		for command in commands:
			command = "".join(command.split('\n')
			command = command.lstrip()
			program.append(command)
	return program

def CheckSyntax(program):
	variableNameRegex = "[a-zA-Z][a-zA-Z0-9]*"
	mutationPattern = re.compile(f"(clear|incr|decr) {variableNameRegex}")
	controlPattern = re.compile(f"(while {variableNameRegex} not 0 do)|end")
	whileCalls = []
	for i,line in enumerate(program):
		if re.fullmatch(controlPattern) is not None:
			if len(line) == 3:
				try:
					frame.pop()
				ecxept _:
					

def main():
	...
if __name__ == '__main__':
	main()
