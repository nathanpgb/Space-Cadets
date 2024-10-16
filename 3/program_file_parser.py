def main():
    # inputPath = input("enter program name: ") 
    inputPath = 'testprogram'
    program = ParseProgramFileByLine(inputPath)
    print(program)

def ParseProgramFile(path):
    path = f"/home/nate/Desktop/Code/Space-Cadets/3/{path}.txt"
    with open(path,"r") as f:
        pureText = f.read()
        colonSeparated = pureText.split(";")
        program = ["programstart"]
        for command in colonSeparated:
            for line in command.split("\n"):
                if line == "":
                    program.append()
                if line[0] == "#":
                    program.append("")
                else:
                    program.append(line)
            
            program.append(command)
        for trailing in reversed(program):
            if trailing == "":
                program.pop()
            elif trailing[0] == "#":
                program.pop()
            else:
                program.append("programend")
                break
    return program

def ParseProgramFileByLine(path):
    path = f"/home/nate/Desktop/Code/Space-Cadets/3/{path}.txt"
    program = ["programstart"]
    with open(path,"r") as f:
        for line in f:
            line = line.lstrip()
            if line ==  "":
                program.append("")
            elif line[0] == "#":
                program.append("")
            else:
                program.append(line.split(";")[0])
    # for endline in reversed(program):
    #     if endline == "":
    #         program.pop()
    program.append("programend")
    return program


if __name__ == '__main__':
    main()