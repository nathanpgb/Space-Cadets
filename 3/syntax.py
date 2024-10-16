import re
numberRegex = "[1-9][0-9]*"
variableNameRegex = "[a-zA-Z](\\w)*"
numericArgumentRegex = f"{numberRegex}|{variableNameRegex}"
numericComparisonOperatorRegex = f"(=|!=|>|>=|<|<=)"
numericComparisonRegex=f".+{numericComparisonOperatorRegex}.+"
numericOperatorRegex = r"\+|-|\*|/"
evaluateableNumericRegex = f"({numericArgumentRegex}{numericOperatorRegex})*{numericArgumentRegex}"
evaluateableBooleanRegex = f"True|False|{numericComparisonRegex}"
evaluateableRegex = f"{evaluateableNumericRegex}|{evaluateableBooleanRegex}"

clearRegex = f"clear {variableNameRegex}"
incrementRegex = f"(incr|decr) {variableNameRegex}( {numberRegex})?"
whileRegex = f"while .+ do"
ifRegex = f"if .+ do"
elseIfRegex = "else if .+ do"
elseRegex = f"else do"
setRegex = f"set {variableNameRegex} to {evaluateableNumericRegex}"
endRegex = "end"

goodAsItIsRegex = f"{clearRegex}|{incrementRegex}|{setRegex}"

goodAsItIsP = re.compile(goodAsItIsRegex)
whileP = re.compile(whileRegex)
ifP = re.compile(ifRegex)
elseIfP = re.compile(elseIfRegex)
elseP = re.compile(elseRegex)
endP = re.compile(endRegex)

