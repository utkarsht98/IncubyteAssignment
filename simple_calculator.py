class SimpleCalculator:
    def __init__(self) -> None:
        self.inputStr = ""
    
    def Add(self, inputString):
        self.inputStr = inputString
        if self.inputStr == "":
            return 0

        