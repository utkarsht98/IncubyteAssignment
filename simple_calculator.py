import re
class SimpleCalculator:
    def __init__(self) -> None:
        self.inputStr = ""
        self.totalSum = 0
    
    # Method to add 2 numbers and return it's sum value
    def Add(self, inputString):
        self.inputStr = inputString

        # Handled empty string case
        if self.inputStr == "":
            return 0
        
        # Handled provided delimiter changes
        if self.inputStr[:2] == "//":
            operands = re.split(self.inputStr[2], self.inputStr[4:])
            print('oeprandndsd==----', operands)

        elif len(self.inputStr.split(",")) == 1: # For single numbers
                return int(self.inputStr)
        else:
            operands = re.split(',|\n', self.inputStr) # For two or more numbers with "," delimiter

        for i in range(len(operands)):
            self.totalSum += int(operands[i])

        return self.totalSum

# inputNumber = input("enter input:")
# calculator = SimpleCalculator()
# print("TotalSum ---> {}".format(calculator.Add(inputNumber)))
