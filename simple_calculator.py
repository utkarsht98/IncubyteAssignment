class SimpleCalculator:
    def __init__(self) -> None:
        self.inputStr = ""
    
    def Add(self, inputString):
        self.inputStr = inputString

        if self.inputStr == "":
            return 0
             
        if len(self.inputStr) == 1:
            return int(self.inputStr)
        else:
            operands = self.inputStr.split(",")
            return int(operands[0])+int(operands[1])