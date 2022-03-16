class SimpleCalculator:
    def __init__(self) -> None:
        self.inputStr = ""
        self.totalSum = 0
    
    # Method to add 2 numbers and return it's sum value
    def Add(self, inputString):
        self.inputStr = inputString

        print(self.inputStr)
        if self.inputStr == "":
            return 0
             
        if "," not in self.inputStr:
            return int(self.inputStr)
        else:
            operands = self.inputStr.split(",")
            for i in range(len(operands)):
                self.totalSum += int(operands[i])
            return self.totalSum

# inputNumber = input("enter input:")
# calculator = SimpleCalculator()
# print("TotalSum ---> {}".format(calculator.Add(inputNumber)))
