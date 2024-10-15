import re
from typing import List,Dict

def OpenFile(path)->List[str]:
	path = f"/home/nate/Desktop/Code/Space-Cadets/2/{path}.txt"
	with open(path,"r") as f:
		pureText = f.read()
		commands = pureText.split(";")
		program = ["programstart"]
		for command in commands:
			command = "".join(command.split('\n'))
			command = command.lstrip()
			program.append(command)
		program[-1] = "programend"
	return program

def RaiseError(message):
	print(message)
	quit()

def CheckSyntax(program:List[str]):
	variableNameRegex = "[a-zA-Z][a-zA-Z0-9]*"
	mutationRegex = f"(clear|incr|decr) {variableNameRegex}"
	mutationPattern = re.compile(mutationRegex)
	forLoopRegex = f"while {variableNameRegex} not 0 do"
	forLoopPattern = re.compile(forLoopRegex)
	headerPattern = re.compile("programstart|programend")
	# controlPattern = re.compile(f"({forLoopRegex})|end")
	whileCalls = []
	for i,line in enumerate(program):
		if re.fullmatch(forLoopPattern,line) is not None:
			tokens = line.split()
			whileCalls.append(i)
		elif line == "end":
			try:
				whileCalls.pop()
			except IndexError:
				RaiseError(f"Error on line {i}: 'end' is unmatched")
		elif re.fullmatch(mutationPattern,line) is not None:
			pass
		elif line =="":
			pass
		elif re.fullmatch(headerPattern,line) is not None:
			if i == 0 and line == "programstart":
				pass
			elif i == len(program)-1 and line == "programend":
				pass
			else:
				RaiseError(f"Error on line{i}: unknown command")
		else:
			RaiseError(f"Error on line {i}: unknown command")	
	if len(whileCalls) != 0:
		line = whileCalls.pop()
		RaiseError(f"While loop declared on line {line} not closed")

def PrintoutVariables(variables:Dict[str,int]):
	for variable in variables:
		print(f"{variable}:{variables[variable]}",end=" ")
	print()

def RunProgram(program:List[str]):
	executingLine = 0
	variables = {}
	whileCalls = []
	searchingForEnd = False
	while True:
		executingLine += 1
		line = program[executingLine]
		tokens = line.split()
		# if tokens == "programstart":
		# 	continue
		# if tokens == "programend":
		# 	print("end")
		# 	PrintoutVariables(variables)
		# 	break

		match tokens[0]:
			case "clear":
				variables[tokens[1]] = 0
			case "incr":
				variableName = tokens[1]
				if variableName in variables:
					variables[variableName] += 1
				else:
					RaiseError(f"Error on line {executingLine}: Variable {variableName} referenced before initialisation")
			case "decr":
				variableName = tokens[1]
				if variableName in variables:
					variables[variableName] -= 1
				else:
					RaiseError(f"Error on line {executingLine}: Variable {variableName} referenced before initialisation")
			case "while":
				variableName = tokens[1]
				if variableName not in variables:
					RaiseError(f"Error on line {executingLine}: Variable {variableName} referenced before initialisation")
				if variables[variableName] == 0:
					searchingForEnd = True
					while searchingForEnd:
						executingLine+=1
						if program[executingLine] == "end":
							searchingForEnd = False
							continue
				else:
					whileCalls.append((variableName,executingLine))
			case "end":
				whileFrame = whileCalls.pop()
				variableName = whileFrame[0]
				if variables[variableName]==0:
					continue
				else:
					executingLine = whileFrame[1]-1

			case "":
				continue
			case "programend":
				print("end")
				PrintoutVariables(variables)
				break
			case _:
				RaiseError(f"unknown error on line {executingLine}:\n{program[executingLine]}")
		PrintoutVariables(variables)
		
def main():
	filePath = input()

	program = OpenFile(filePath)
	CheckSyntax(program)
	RunProgram(program)
	
if __name__ == '__main__':
	main()
