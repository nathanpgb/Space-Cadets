from ProgramFileParser import ParseProgramFile
from interpreter import Run, CheckSyntax

def main():
    # filename = input("enter program file name: ")
    filename = "testprogram"
    program = ParseProgramFile(filename)
    print(program)
    CheckSyntax(program)
    Run(program)

if __name__ == "__main__":
    main()