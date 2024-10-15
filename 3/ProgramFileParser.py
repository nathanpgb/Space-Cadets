def main():
    # inputPath = input("enter program name: ") 
    inputPath = 'testprogram'
    program = ParseProgramFile(inputPath)
    print(program)

def ParseProgramFile(path):
    path = f"/home/nate/Desktop/Code/Space-Cadets/3/{path}.txt"
    with open(path,"r") as f:
        pureText = f.read()
        colonSeparated = pureText.split(";")
        program = ["programstart"]
        for command in colonSeparated:
            command = command.split("\n")[-1]
            
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

if __name__ == '__main__':
    main()