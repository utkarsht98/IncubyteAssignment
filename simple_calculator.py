from mimetypes import init
import re
class SimpleCalculator:
    def __init__(self) -> None:
        self.inputStr = ""
        self.totalSum = 0
        self.operands = []
    
    # Method to add 2 numbers and return it's sum value
    def Add(self, inputString):
        self.inputStr = inputString
        
        # Handled empty string case
        if self.inputStr == "":
            return 0
        
        # Handled provided delimiter changes
        if self.inputStr[:2] == "//":
            self.operands = re.split(self.inputStr[2], self.inputStr[4:])
            print('oeprandndsd==----', self.operands)

        elif len(self.inputStr.split(",")) == 1: # For single numbers
                return int(self.inputStr)
        else:
            self.operands = re.split(',|\n', self.inputStr) # For two or more numbers with "," delimiter
            print('\n delimiter', self.operands)

        try:
            for i in range(len(self.operands)):
                if int(self.operands[i]) < 0:
                    raise NegativeValueError(self.operands)
                self.totalSum += int(self.operands[i])

        except NegativeValueError as e:
            message = "Negatives not allowed --->" + e.getNegativeNumbers()
            return message

        return self.totalSum

class Error(Exception):
    """Base class for other exceptions"""
    pass

class NegativeValueError(Error):
    """ Raised when the numerical values is Negative"""
    def __init__(self, operands) -> None:
        self.operands = operands
    
    def getNegativeNumbers(self):
        negNumString = ""
        for i in range(len(self.operands)):
            if int(self.operands[i]) < 0:
                negNumString += self.operands[i] + ","
        return negNumString[:-1]

# inputNumber = input("enter input:")
# calculator = SimpleCalculator()
# print("TotalSum ---> {}".format(calculator.Add(inputNumber)))
