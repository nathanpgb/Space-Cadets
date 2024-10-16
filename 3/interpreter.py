import re
from typing import List,Dict,Tuple
from abc import ABC
from syntax import goodAsItIsP,ifP,elseIfP,elseP,whileP,endP

class Branch(ABC):
    def __init__(self,startLine):
        self.__startLine = startLine
        self.__endLine = -1
        
class WhileBranch(Branch):
    def __init__(self,startLine,condition):
        super().__init__(startLine)
        self.__condition = condition

class BranchStack():
    def __init__(self):
        self.__stack:List[Branch] = []
    
    def AddCall(self,callType,line):
        match type:
            case "while":
                self.__stack.append((callType,line))
            case "if":
                self.__stack.append((callType,[line],True))
            case "else":
                if self.__stack[-1][0] == "if":
                    self.__stack[-1][1].append(line)
            case "end":
                pass

            
def RaiseSyntaxError(line,program,message="Invalid Syntax"):
    print(f"Syntax error on line {line}:\n{program[line]}\n{message}")
    quit()
            


def CheckSyntax(program:List[str]):
    branchStack = []

    for i,line in enumerate(program[1:-1],1):
        tokens = line.split()
        #begin lots of ifs 
        if re.fullmatch(whileP,line):
            branchStack.append(("while",i))
        elif re.fullmatch(ifP,line):
            branchStack.append(("if",i))
        elif re.fullmatch(elseIfP,line):
            if branchStack[-1][0] in ("if","else if"):
                branchStack.append(("else if",i))
            else:
                RaiseSyntaxError(i,program,"else if has no valid preceding if")     
        elif re.fullmatch(elseP,line):
            if branchStack[-1][0] in ("if","else if"):
                branchStack.append(("else",i))
            else:
                RaiseSyntaxError(i,program,"else has no valid preceeding if")
        elif re.fullmatch(endP,line):
            try:
                lastBranch = branchStack.pop()
            except IndexError:
                RaiseSyntaxError(i,program,"unmatched end")
            else:
                while lastBranch[0] in ("else","else if"):
                    lastBranch = branchStack.pop()
                    
        elif re.fullmatch(goodAsItIsP,line):
            pass
        elif line == "":
            pass
        else:
            RaiseSyntaxError(i,program,"line does not match any valid syntax")
            



def Run(program):
    ...

def main():

    CheckSyntax("testprogram")