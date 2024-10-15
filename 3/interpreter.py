import re
from typing import List,Dict,Tuple
from abc import ABC

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
    numberRegex = "[1-9][0-9]*"
    variableNameRegex = "[a-zA-Z][a-zA-Z0-9]*"
    numericArgumentRegex = f"{numberRegex}|{variableNameRegex}"
    numericComparisonRegex = f"(=|!=|>|>=|<|<=)"
    numericOperatorRegex = r"\+|\-|\*|\/"
    # basicNumericExpressionRegex = f"{valueArgumentRegex} {numericOperatorRegex} {valueArgumentRegex}"
    evaluateableNumericRegex = f"({numericArgumentRegex} {numericOperatorRegex})+ {numericArgumentRegex}"
    evaluateableBooleanRegex = f"True|False|({evaluateableNumericRegex} {numericComparisonRegex} {evaluateableNumericRegex})"
    evaluateableRegex = f"{evaluateableNumericRegex}|{evaluateableBooleanRegex}"

    clearRegex = f"clear {variableNameRegex}"
    incrementRegex = f"(incr|decr) {variableNameRegex} {numberRegex}"
    whileRegex = f"while {evaluateableBooleanRegex} do"
    ifRegex = f"if {evaluateableBooleanRegex} do"

    elseIfRegex = f"else if {evaluateableBooleanRegex} do"
    elseRegex = f"else do"
    setRegex = f"set {variableNameRegex} to {evaluateableNumericRegex}"
    endRegex = "end"

    goodAsItIsRegex = f"{clearRegex}|{incrementRegex}|{setRegex}"

    branchStack = []

    for i,line in enumerate(program[1:-1],1):
        tokens = line.split()
        #begin lots of ifs 
        if re.fullmatch(goodAsItIsRegex,line):
            pass
        elif re.fullmatch(whileRegex,line):
            branchStack.append(("while",i))
        elif re.fullmatch(ifRegex,line):
            branchStack.append(("if",i))
        elif re.fullmatch(elseIfRegex,line):
            if branchStack[-1][0] in ("if","elseIf"):
                branchStack.append(("elseIf",i))
            else:
                RaiseSyntaxError(i,program)     
        elif re.fullmatch(elseRegex,line):
            if branchStack[-1][0] in ("if","elseIf"):
                branchStack.append(("else",i))
            else:
                RaiseSyntaxError(i,program)
        elif re.fullmatch(endRegex,line):
            try:
                lastBranch = branchStack.pop()
            except IndexError:
                RaiseSyntaxError(i,program)
            else:
                while lastBranch[0] in ("else","elseIf"):
                    lastBranch = branchStack.pop()
                if lastBranch[0] == "if":
                    branchStack.pop()
        else:
            RaiseSyntaxError(i,program)
            



def Run(program):
    ...